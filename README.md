# LangChain and LangGraph Learning Project

This project contains examples and experiments for learning LangChain and LangGraph frameworks.

## Setup

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone or navigate to this directory
2. Initialize uv project:
   ```bash
   uv init --python 3.12
   ```
3. Install dependencies:
   ```bash
   uv add langgraph langchain langchain-anthropic langchain-openai python-dotenv ipython
   ```
4. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   cp .env.example .env
   ```
5. Edit `.env` file with your actual API keys:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude models
   - `OPENAI_API_KEY`: Your OpenAI API key (optional)
   - `LANGSMITH_API_KEY`: Your LangSmith API key for tracing and debugging
   - `LANGSMITH_PROJECT`: Project name for organizing traces (e.g., "new-agent")

## Examples

### Basic Examples

#### Simple LangGraph Workflow (`examples/basic/hello.py`)
A simple LangGraph workflow that demonstrates:
- Creating a StateGraph with MessagesState
- Adding nodes and edges
- Basic graph execution with logging

Run with:
```bash
uv run python examples/basic/hello.py
```

### Agent Examples

#### Functional API Agent (`examples/agents/first_agent_functional_API_usage.py`)
An agent using LangGraph's functional API that can perform arithmetic operations:
- Uses `@task` and `@entrypoint` decorators
- Integration with Anthropic's Claude model
- Tool binding for mathematical operations (add, multiply, divide)
- Streaming responses with built-in parallelization

Run with:
```bash
uv run python examples/agents/first_agent_functional_API_usage.py
```

#### Graph API Agent (`examples/agents/first_agent_graph_API_usage.py`)
An agent using LangGraph's graph API with explicit state management:
- Custom state class with typed fields
- Conditional edges for flow control
- Graph visualization saved to `images/` folder
- Detailed state tracking (including LLM call counts)

Run with:
```bash
uv run python examples/agents/first_agent_graph_API_usage.py
```

### LangGraph Project Template (`examples/langgraph_project/`)
A complete **arithmetic agent** built with LangGraph that demonstrates:
- **Multi-node architecture** with conditional routing
- **Tool calling** for mathematical operations (add, multiply, divide)
- **Natural language understanding** using Anthropic's Claude
- **Runtime configuration** for customizable behavior
- **Professional project structure** with tests and CI/CD
- **Production-ready** deployment capabilities

**Key Features:**
- Understands math requests in natural language
- Uses tools for precise calculations
- Makes intelligent decisions about when to call tools
- Supports runtime configuration per conversation
- Tracks conversation history and execution metrics

To set up and run the LangGraph server:
```bash
cd examples/langgraph_project
uv add --dev .  # Install project in editable mode
uv run langgraph dev
```

This starts a local development server with:
- **🚀 API**: http://127.0.0.1:2024
- **🎨 Studio UI**: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- **📚 API Docs**: http://127.0.0.1:2024/docs

The server includes:
- In-memory runtime for development and testing
- LangGraph Studio integration for visual debugging
- Hot reload for local changes
- Thread management and monitoring
- Integration with LangSmith for tracing (when API key is configured)

## Development Workflow

### Using LangGraph Studio
1. Start the development server: `cd examples/langgraph_project && uv run langgraph dev`
2. Open LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
3. Create a new thread to start testing your arithmetic agent
4. Try natural language math requests:
   - "Add 15 and 27"
   - "What is 8 times 9?"
   - "Calculate (25 + 17) * 3"
5. Configure the agent with custom settings:
   ```json
   {
     "system_prompt": "You are a patient math tutor. Always explain your steps.",
     "temperature": 0.1
   }
   ```
6. Use the visual debugger to:
   - Watch nodes execute in real-time
   - Inspect state changes between nodes
   - See tool calling decisions
   - Step through conditional routing
   - Edit and replay from any point
7. Edit code locally - changes are automatically reloaded

### Local Development
- All examples can be run directly: `uv run python examples/basic/hello.py`
- The LangGraph project includes comprehensive tests: `cd examples/langgraph_project && uv run pytest`
- Graph visualizations are saved to the `images/` directory
- LangSmith tracing provides detailed execution logs when API key is configured

## Project Structure
```
.
├── .env                                    # Environment variables (not tracked in git)
├── .env.example                           # Environment variables template
├── examples/                              # Example implementations
│   ├── basic/                            # Basic LangGraph examples
│   │   └── hello.py                      # Simple workflow example
│   ├── agents/                           # Agent implementations
│   │   ├── first_agent_functional_API_usage.py  # Functional API agent
│   │   └── first_agent_graph_API_usage.py       # Graph API agent
│   └── langgraph_project/               # Complete LangGraph project template
│       ├── src/agent/graph.py           # Core graph implementation
│       ├── tests/                       # Unit and integration tests
│       ├── langgraph.json              # LangGraph configuration
│       └── README.md                   # Project-specific documentation
├── images/                                # Generated graph visualizations
├── pyproject.toml                         # uv project configuration
└── README.md                             # This file
```

## Dependencies
- **langchain**: Core LangChain framework
- **langgraph**: Graph-based agent framework
- **langgraph-cli[inmem]**: LangGraph CLI with in-memory backend for local development
- **langchain-anthropic**: Anthropic Claude integration
- **langchain-openai**: OpenAI integration
- **python-dotenv**: Environment variable management
- **ipython**: Enhanced Python REPL and visualization support

## Learning Outcomes

This project demonstrates key LangGraph concepts:

### 🏗️ **Architecture Patterns**
- **Conditional Routing**: Decision-making with `should_continue` functions
- **Tool Integration**: Seamless LLM-tool interaction loops
- **State Management**: Tracking conversation and execution state
- **Runtime Configuration**: Dynamic behavior customization

### 🛠️ **Production Practices**
- **Testing Strategy**: Unit and integration tests
- **Development Workflow**: Hot reload and visual debugging
- **Deployment Ready**: Professional project structure
- **Observability**: LangSmith tracing integration

### 🎯 **Extensibility Examples**
From this arithmetic agent foundation, you can build:
- **Web Search Agents**: Replace math tools with search APIs
- **Data Analysis Bots**: Add pandas/plotting tools
- **Code Assistants**: Include code execution tools
- **Multi-Modal Agents**: Add image/document processing

## Next Steps
- Explore more complex LangGraph workflows
- Implement multi-agent systems
- Add memory and persistence
- Create advanced tool integrations
- Build domain-specific agents using this template