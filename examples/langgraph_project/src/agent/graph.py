"""LangGraph arithmetic agent with tool calling capabilities.

An agent that can perform mathematical operations using tools.
Integrates with Anthropic's Claude model for natural language understanding.
"""

from __future__ import annotations

import operator
import os
from typing import Any, Dict, Literal

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import AnyMessage, HumanMessage, SystemMessage, ToolMessage
from langchain.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.runtime import Runtime
from typing_extensions import TypedDict, Annotated

# Load environment variables
load_dotenv()


class Context(TypedDict):
    """Context parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    """

    model_name: str
    temperature: float
    system_prompt: str


class MessagesState(TypedDict):
    """State for the arithmetic agent.

    Tracks conversation messages and LLM call count.
    """

    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int


# Define mathematical tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b


@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b


# Tool setup
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}


def get_model(runtime: Runtime[Context]):
    """Get configured model with tools."""
    context = runtime.context or {}
    model_name = context.get("model_name", "claude-sonnet-4-5-20250929")
    temperature = context.get("temperature", 0)

    model = init_chat_model(model_name, temperature=temperature)
    return model.bind_tools(tools)


def llm_call(state: MessagesState, runtime: Runtime[Context]) -> Dict[str, Any]:
    """LLM decides whether to call a tool or not."""
    context = runtime.context or {}
    system_prompt = context.get(
        "system_prompt",
        "You are a helpful assistant tasked with performing arithmetic on a set of inputs."
    )

    model_with_tools = get_model(runtime)

    system_message = SystemMessage(content=system_prompt)
    messages = [system_message] + state["messages"]

    response = model_with_tools.invoke(messages)

    return {
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }


def tool_node(state: MessagesState, runtime: Runtime[Context]) -> Dict[str, Any]:
    """Performs the tool calls."""
    result = []
    last_message = state["messages"][-1]

    for tool_call in last_message.tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=str(observation), tool_call_id=tool_call["id"]))

    return {"messages": result}


def should_continue(state: MessagesState, runtime: Runtime[Context]) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call."""
    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END


# Build the graph
graph = (
    StateGraph(MessagesState, context_schema=Context)
    .add_node("llm_call", llm_call)
    .add_node("tool_node", tool_node)
    .add_edge(START, "llm_call")
    .add_conditional_edges(
        "llm_call",
        should_continue,
        ["tool_node", END]
    )
    .add_edge("tool_node", "llm_call")
    .compile(name="Arithmetic Agent")
)
