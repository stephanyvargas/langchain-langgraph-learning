import pytest
from langchain.messages import HumanMessage

from agent import graph

pytestmark = pytest.mark.anyio


@pytest.mark.langsmith
async def test_agent_arithmetic() -> None:
    """Test the arithmetic agent with a simple addition problem."""
    inputs = {
        "messages": [HumanMessage(content="Add 3 and 4")],
        "llm_calls": 0
    }

    res = await graph.ainvoke(inputs)

    assert res is not None
    assert "messages" in res
    assert len(res["messages"]) > 0
    assert res["llm_calls"] > 0


@pytest.mark.langsmith
async def test_agent_with_context() -> None:
    """Test the agent with custom context configuration."""
    inputs = {
        "messages": [HumanMessage(content="What is 5 times 6?")],
        "llm_calls": 0
    }

    context = {
        "model_name": "claude-sonnet-4-5-20250929",
        "temperature": 0,
        "system_prompt": "You are a mathematical assistant. Always show your work."
    }

    res = await graph.ainvoke(inputs, config={"configurable": context})

    assert res is not None
    assert "messages" in res
    assert res["llm_calls"] > 0
