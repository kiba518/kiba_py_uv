from fastapi import FastAPI
from starlette.responses import HTMLResponse
from app.routers import api_test, items
import socket
app = FastAPI(title="Kiba Demo API")
app.include_router(api_test.router)
app.include_router(items.router)

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






