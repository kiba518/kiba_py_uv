
from mcp.server.sse import SseServerTransport
from starlette.routing import Mount
from .tool_weather import mcp
from fastapi import APIRouter, Depends, Request, Form, Query


router_sse = APIRouter(prefix="", tags=["mcp操作"])


# Create SSE transport instance for handling server-sent events
sse = SseServerTransport("/messages/")

# Mount the /messages path to handle SSE message posting
# router_sse.add_api_route("/messages", sse.handle_post_message, methods=["POST"])
# router_sse.routes.append(Mount("/messages", app=sse.handle_post_message))

# Add documentation for the /messages endpoint
@router_sse.get("/messages", tags=["MCP"], include_in_schema=True)
def messages_docs():
    """
    Messages endpoint for SSE communication

    This endpoint is used for posting messages to SSE clients.
    Note: This route is for documentation purposes only.
    The actual implementation is handled by the SSE transport.
    """
    pass  # This is just for documentation, the actual handler is mounted above


@router_sse.get("/handle", tags=["MCP"])
async def handle_sse(request: Request):
    """
    SSE endpoint that connects to the MCP server

    This endpoint establishes a Server-Sent Events connection with the client
    and forwards communication to the Model Context Protocol server.
    """
    # Use sse.connect_sse to establish an SSE connection with the MCP server
    async with sse.connect_sse(request.scope, request.receive, request._send) as (
        read_stream,
        write_stream,
    ):
        # Run the MCP server with the established streams
        await mcp._mcp_server.run(
            read_stream,
            write_stream,
            mcp._mcp_server.create_initialization_options(),
        )



