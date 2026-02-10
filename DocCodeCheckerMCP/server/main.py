import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fastmcp import FastMCP
from server.handlers import (
    read_swagger_spec,
    extract_code_tokens_handler,
    compare_spec_and_code
)

mcp = FastMCP(name="DocCode Checker MCP")

mcp.tool()(read_swagger_spec)
mcp.tool(name="extract_code_tokens")(extract_code_tokens_handler)
mcp.tool()(compare_spec_and_code)

if __name__ == "__main__":
    mcp.run(transport="stdio")