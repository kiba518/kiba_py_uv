from mcp.server.fastmcp import FastMCP

mcp = FastMCP("general")

# 2. 显式导入你的两个工具文件中的工具实例
# 这会强制 Python 解释器加载并执行这两个文件
from .tool_database import mcp
from .tool_weather import mcp