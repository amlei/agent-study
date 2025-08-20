# # server.py
# from mcp.server.fastmcp import FastMCP

# # Create an MCP server
# mcp = FastMCP("Demo")


# # Add an addition tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b


# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")~
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

# 示例代码（calculator_server.py）
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("计算器")

@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")  # 关键启动语句