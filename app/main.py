from fastapi import FastAPI
from starlette.responses import HTMLResponse
from app.routers  import api_router
from starlette.routing import Mount
from app.routers.mcp.sse import sse
import socket

app = FastAPI(
    title="Kiba Demo API",
    description="A demonstration of Server-Sent Events with Model Context and API Invoke "
    "Protocol integration",
    version="0.1.0",
)

app.router.routes.append(Mount("/messages", app=sse.handle_post_message)) # 这个得单独挂，在router里挂载，url就对不上
app.include_router(api_router)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <form method="POST" action="/submit">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    """

# ✅ 自动获取本机 IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 5001

print("\n🚀 Server running!")
print(f"🔹 Swagger UI: http://{local_ip}:{port}/docs")
print(f"🔹 ReDoc:      http://{local_ip}:{port}/redoc\n")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)






