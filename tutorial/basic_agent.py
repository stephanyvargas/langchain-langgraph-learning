from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph, MessagesState
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
#from langgraph.checkpoint.memory import MemorySaver # should not be used with langsmith
from langgraph.prebuilt import ToolNode
from typing import Literal

load_dotenv()
#checkpointer = MemorySaver()

@tool
def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["munich"]:
        return "It's 15 degrees Celsius and cloudy."
    else:
        return "It's 32 degrees Celsius and sunny."

def call_model(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

tools = [get_weather]
model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
tool_node = ToolNode(tools)

workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
)
workflow.add_edge("tools", "agent")

graph = workflow.compile() # checkpointer=checkpointer) # dont use checkpointers with langsmith
#value ={
#        "messages": [
#            HumanMessage(content="How is the weather in munich?")
#        ]
#    }
#print(graph.invoke(value))
