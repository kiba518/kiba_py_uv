## 创建项目步骤

#### 安装uv

windows+r运行powershell，然后运行

```
irm https://astral.sh/uv/install.ps1 | iex
```

![1762240855732](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762240855732.png)

安装后检查：

```
uv --version
```

看到版本号（例如 `uv 0.5.9`）说明成功。

#### 创建项目

windows+r运行cmd，然后运行

```
uv init kiba_py_uv
```

![1762240835390](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762240835390.png)

然后创建了项目

![1762240891738](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762240891738.png)

#### 打开项目

使用pycharm打开项目，然后，打开终端，再重新执行

```
pip install uv
```

这次是在.venv里安装uv。

然后执行

```
uv add fastapi
uv add python-multipart
uv add uvicorn

```

然后再pyproject.toml里就会自动增加依赖项。

![1762243628199](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762243628199.png)

然后再新建app/routers文件夹，然后创建文件tests.py。然后编写内容：

```
from fastapi import APIRouter, Depends, Request, Form, Query

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/{webhook}")
async def handle_webhook(webhook: str, request: Request):
    data = await request.json()  # ✅ 获取 JSON 请求体
    print(f"Webhook path: {webhook}")
    print("Received Webhook data:", data)
    return {"data": "Webhook received!"}


# 🔍 处理 GET 请求，获取 query 参数
@router.get("/search")
def search(
        q: str = Query(default="", description="搜索关键词"),
        page: int = Query(default=1, description="页码")
):
    return {"message": f"Search query: {q}, Page: {page}"}


# 📩 处理 POST 请求，接收表单数据
@router.post("/submit")
def submit(name: str = Form(...)):
    return {"message": f"Hello, {name}! Your form has been submitted."}
 
```

即便在项目里使用工具安装，依然会安装到依赖里。

![1762244059631](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762244059631.png)

#### 修改依赖

如果想删除依赖，只需要去dependencies里删除依赖即可。

![1762245571012](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762245571012.png)

然后执行下面命令，更新依赖

```
uv sync
```

#### 编写main

代码如下：

```
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
```

#### 启动项目

打开终端，执行下面命令启动项目。

```
uv run python -m app.main
```

【推荐】启动命令

这个命令可以替换main的指定端口。

````
uvicorn app.main:app --reload --port 5001
````

而且可以在调试配置里设置启动。

![1762247565662](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762247565662.png)

#### 整体项目结构

![1762247611775](C:\GitHub\Kiba-Py-Uv\kiba_py_uv\README.assets\1762247611775.png)