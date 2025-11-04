from fastapi import FastAPI
from starlette.responses import HTMLResponse
from app.routers import tests

app = FastAPI(title="Kiba Demo API")
app.include_router(tests.router)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <form method="POST" action="/submit">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    """



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)






