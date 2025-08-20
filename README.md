# Project Overview

This directory, `Agent-Study`, is dedicated to learning and experimenting with AI Agent development. The primary focus is on building agents using Python, with key technologies including LangChain, LangGraph, and potentially the Model Context Protocol (MCP). The goal, as indicated by the `.github/copilot-instructions.md` file, is to become proficient in Agent development and assist others in learning it, primarily using Chinese.

# Key Technologies and Frameworks

*   **LangChain/LangGraph**: Used for building complex AI agent workflows. Notebooks in `langgraph_study` demonstrate core concepts like ReAct agents, memory management, structured output, and human-in-the-loop interactions.
*   **Pydantic-AI**: Used in the `ai-agent-demo` for creating simpler agents with tool calling capabilities, interacting with models like Google's Qwen.
*   **Model Context Protocol (MCP)**: Indicated by the `server.py` file and the `ai-mcp-demo`, suggesting exploration of the standard for integrating tools and resources with AI models.

# Directory Structure and Contents

*   `langgraph_study/`: Contains Jupyter Notebooks (`quickstarts.ipynb`) exploring LangGraph concepts. This is a core learning resource for building stateful, graph-based agents.
*   `demo/`:
    *   `ai-agent-demo/`: Examples of simpler agents built with Pydantic-AI (`main.py`, `tools.py`).
    *   `ai-mcp-demo/`: Likely examples related to the Model Context Protocol.
*   `server.py`: A basic example of an MCP server, potentially for exposing tools or resources to an AI model.
*   `tests/`: Likely contains test cases for the various agent implementations and libraries explored.
*   `.github/copilot-instructions.md`: Defines the role and expertise level for AI assistance within this repository (Agent expert, LangChain/LangGraph, Chinese responses).

# Development and Learning Approach

1.  **LangGraph Exploration**: Start by studying the `langgraph_study/quickstarts.ipynb` notebook to understand advanced agent patterns.
2.  **Pydantic-AI Examples**: Review the `demo/ai-agent-demo` for simpler agent structures and tool usage.
3.  **MCP Integration**: Investigate `server.py` and `demo/ai-mcp-demo` for understanding the Model Context Protocol.
4.  **Experimentation**: Use the `tests` directory to validate concepts and ensure code correctness.

# Usage

This directory serves as a learning environment. Users can explore the provided examples, run the Jupyter notebooks, and experiment with the agent demos to understand different agent architectures and integration techniques. The `.github/copilot-instructions.md` file provides context for how an AI assistant should behave when helping within this project.