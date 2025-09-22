import gradio as gr
import os
from mcp import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection, MCPClient
from smolagents.mcp_client import MCPClient

# with MCPClient(
#     {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"}
# ) as tools:
#     # Tools from the remote server are available
#     print("\n".join(f"{t.name}: {t.description}" for t in tools))

mcp_client = MCPClient(
    {
        "url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"
    }  # This is the MCP Client we created in the previous section
)
tools = mcp_client.get_tools()
