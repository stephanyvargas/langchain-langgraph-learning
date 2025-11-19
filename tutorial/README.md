# LangGraph Tutorial Collection

This repository contains a comprehensive collection of Jupyter notebooks and supporting projects showcasing **LangGraph**, a Python library for building and managing agents with graph-based workflows.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Environment with LangGraph dependencies (see main project README)

## Setup

This tutorial collection is designed to work within the main project environment. From the project root:

```bash
# Ensure all dependencies are installed
uv add jupyter chromadb fastapi uvicorn pytest pytest-asyncio psycopg2-binary

# Navigate to tutorial directory
cd tutorial/
```

## Running Tutorials

### 🚀 **Interactive Jupyter Notebooks**
```bash
# Start Jupyter for interactive learning
uv run jupyter notebook

# Run specific tutorial
uv run jupyter notebook 01_Basics.ipynb
```

### 🎨 **LangGraph Studio Integration**
For visual debugging and agent development:

```bash
# Run the basic agent with LangSmith Studio
uv run langgraph dev

# Access Studio UI at: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
# API Docs: http://127.0.0.1:2024/docs
```

### 🧪 **Testing Framework**
```bash
# Run tutorial unit tests
uv run pytest unit_tests/

# Run with verbose output
uv run pytest unit_tests/ -v
```

## Notebooks

- **00_TypedDict.ipynb**
  Explanation of the differences between `TypedDict` and Pydantic for managing state.

- **01_Basics.ipynb**
  Introduction to the basic concepts of LangGraph, including how to build simple agent workflows.

- **02_Tool_calling_basics.ipynb**
  Demonstrates how to enable agents to call tools effectively within LangChain (not LangGraph!).

- **03_Agent_basics.ipynb**
  Explores the fundamental features of creating and managing agents using LangGraph.

- **RAG_Basics.ipynb**
  Overview of Retrieval-Augmented Generation (RAG) basics with LangGraph.

- **RAG_Agent.ipynb**
  Implementation of an agent that leverages RAG for enhanced information retrieval.

- **RAG_Agent_with_memory.ipynb**
  Shows how to extend a RAG agent with memory capabilities for contextual responses.

- **Advanced_State.ipynb**
  Advanced techniques for managing agent states within LangGraph workflows.

- **Human_in_the_Loop.ipynb**
  Incorporates human input into LangGraph workflows for guided decision-making.

- **ParallelExecution.ipynb**
  Demonstrates parallel execution of nodes in LangGraph for efficient processing.

- **AsyncAndStreaming.ipynb**
  Explores asynchronous execution and streaming outputs in LangGraph workflows.

- **Subgraphs.ipynb**
  Illustrates how to use subgraphs to modularize and reuse parts of a workflow.

- **Agent_Patterns.ipynb**
  Showcases common agent design patterns and reusable templates.

- **LongTermMemory.ipynb**
  Implements long-term memory functionality in agents using LangGraph.

## Additional Content

### unit_tests

**Description**: Demonstrates how to test LangGraph apps effectively.

- Includes examples of unit tests for LangGraph nodes.

## Example Implementations

### **basic_agent.py**
A complete weather agent implementation demonstrating:
- Tool calling with OpenAI GPT-4o-mini
- Conditional routing based on tool calls
- LangSmith Studio integration via `langgraph.json`

```bash
# Run with LangSmith Studio
uv run langgraph dev
```

### **unit_tests/**
**Description**: Demonstrates how to test LangGraph apps effectively.
- Includes examples of unit tests for LangGraph nodes
- Testing patterns for state management and node execution

### **fullstackapp/**
**Description**: Capstone project demonstrating the integration of a full-stack application with a human-in-the-loop workflow.

- **Frontend**: Built with Angular
- **Backend**: Built with FastAPI (async!)
- **Database**: PostgreSQL
- **Docker**: Multi-service deployment with docker-compose

```bash
# Run fullstack app
cd fullstackapp/
docker-compose up
```

## Environment Configuration

Ensure your `.env` file (in project root) contains:
```bash
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
LANGSMITH_API_KEY=your_langsmith_key  # Optional for tracing
LANGSMITH_PROJECT=tutorial-project    # Optional
```
