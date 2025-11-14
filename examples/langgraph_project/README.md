# New LangGraph Project

[![CI](https://github.com/langchain-ai/new-langgraph-project/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/langchain-ai/new-langgraph-project/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/langchain-ai/new-langgraph-project/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/langchain-ai/new-langgraph-project/actions/workflows/integration-tests.yml)

This template demonstrates an **arithmetic agent** implemented using [LangGraph](https://github.com/langchain-ai/langgraph), designed for showing how to get started with [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server) and using [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/), a visual debugging IDE.

<div align="center">
  <img src="./static/studio_ui.png" alt="Graph view in LangGraph studio UI" width="75%" />
</div>

The core logic defined in `src/agent/graph.py`, showcases a **multi-node agent** that:

- **Understands natural language** math requests using Anthropic's Claude
- **Uses tools** for mathematical operations (add, multiply, divide)
- **Makes decisions** about whether to call tools or respond directly
- **Supports runtime configuration** for model selection and behavior
- **Tracks state** including conversation history and LLM call counts

You can extend this graph to orchestrate more complex agentic workflows that can be visualized and debugged in LangGraph Studio.

## Getting Started

1. Install dependencies, along with the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/), which will be used to run the server.

```bash
cd path/to/your/app
pip install -e . "langgraph-cli[inmem]"
```

2. (Optional) Customize the code and project as needed. Create a `.env` file if you need to use secrets.

```bash
cp .env.example .env
```

If you want to enable LangSmith tracing, add your LangSmith API key to the `.env` file.

```text
# .env
LANGSMITH_API_KEY=lsv2...
```

3. Start the LangGraph Server.

```shell
langgraph dev
```

For more information on getting started with LangGraph Server, [see here](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/).

## Usage Examples

### Basic Usage
Try asking the agent to perform mathematical operations:
- "Add 15 and 27"
- "What is 8 times 9?"
- "Divide 144 by 12"
- "Calculate 25 + 17 - 8"

### Configuration
The agent supports runtime configuration:

```python
# Custom system prompt
context = {
    "system_prompt": "You are a patient math tutor. Always explain your steps.",
    "model_name": "claude-sonnet-4-5-20250929",
    "temperature": 0.1
}

# Use in LangGraph Studio or via API
```

### Graph Structure
The agent uses a **conditional loop** pattern:
1. **LLM Call**: Analyzes user input and decides whether to use tools
2. **Tool Execution**: Performs mathematical operations when needed
3. **Decision Point**: Continue with tools or return final answer

## How to customize

1. **Define runtime context**: Modify the `Context` class in the `graph.py` file to expose the arguments you want to configure per assistant. For example, in a chatbot application you may want to define a dynamic system prompt or LLM to use. For more information on runtime context in LangGraph, [see here](https://langchain-ai.github.io/langgraph/agents/context/?h=context#static-runtime-context).

2. **Extend the graph**: The core logic of the application is defined in [graph.py](./src/agent/graph.py). You can modify this file to add new nodes, edges, or change the flow of information.

## Development

While iterating on your graph in LangGraph Studio, you can edit past state and rerun your app from previous states to debug specific nodes. Local changes will be automatically applied via hot reload.

Follow-up requests extend the same thread. You can create an entirely new thread, clearing previous history, using the `+` button in the top right.

For more advanced features and examples, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/). These resources can help you adapt this template for your specific use case and build more sophisticated conversational agents.

LangGraph Studio also integrates with [LangSmith](https://smith.langchain.com/) for more in-depth tracing and collaboration with teammates, allowing you to analyze and optimize your chatbot's performance.

