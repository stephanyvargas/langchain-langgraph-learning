from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    print(f"Mock LLM received state: {state}")
    response = {"messages": [{"role": "ai", "content": "hello world"}]}
    print(f"Mock LLM returning: {response}")
    return response

print("Creating graph...")
graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()
print("Graph compiled successfully!")

print("Invoking graph...")
result = graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
print(f"Final result: {result}")
