## 创建项目步骤

#### 安装uv

windows+r运行powershell，然后运行

```
irm https://astral.sh/uv/install.ps1 | iex
```

![1762240855732](C:\GitHub\kiba_py_uv\README.assets\1762240855732.png)

安装后检查：

```
uv --version
```

看到版本号（例如 `uv 0.5.9`）说明成功。

#### 安装方法二【未测试】

也可以执行pipx，这样会在电脑用户的下创建一个文件夹，比如C:\Users\kiba.local\pipx\venvs\uv\。

然后再path里增加该地址。

```
pipx install uv
```

#### 创建项目

windows+r运行cmd，然后运行

```
uv init kiba_py_uv
```

![1762240835390](C:\GitHub\kiba_py_uv\README.assets\1762240835390.png)

然后创建了项目

![1762240891738](C:\GitHub\kiba_py_uv\README.assets\1762240891738.png)

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

![1762243628199](C:\GitHub\kiba_py_uv\README.assets\1762243628199.png)

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

![1762244059631](C:\GitHub\kiba_py_uv\README.assets\1762244059631.png)

#### 激活环境

激活环境后，下载的包就都下载到.venv里了，能确保独立环境，以免出现奇怪的bug

```
.venv\Scripts\Activate.ps1
```

其实就是执行了个脚本。

![1762926430081](C:\GitHub\kiba_py_uv\README.assets\1762926430081.png)

#### 修改依赖

如果想删除依赖，只需要去dependencies里删除依赖即可。

![1762245571012](C:\GitHub\kiba_py_uv\README.assets\1762245571012.png)

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

这个命令可以替换main的指定端口。【uvicorn只是针对使用 ASGI 服务器（异步），通过 `app` 对象启动。也就是使用fastapi开发的项目】

````
uvicorn app.main:app --reload --port 5001
````

而且可以在调试配置里设置启动。

![1762247565662](C:\GitHub\kiba_py_uv\README.assets\1762247565662.png)

也可以配置FastApi，他也是执行uvicorn。【注意 python 解释器，一定要选择自己的.venv，不然加载不了我们之前同步的轮子】

![1762303647026](C:\GitHub\kiba_py_uv\README.assets\1762303647026.png)

执行结果

![1762303672790](C:\GitHub\kiba_py_uv\README.assets\1762303672790.png)

#### 整体项目结构

![1762247611775](C:\GitHub\kiba_py_uv\README.assets\1762247611775.png)

#### 新项目初始化

新项目初始化，执行

```
uv sync
```

就会自动下载依赖库。



## 启动ragflow的一些异常

#### 指定python版本创建venv，有时候安装了新版python，但uv就是使用旧版本创建环境

```
uv sync --python C:\Users\jinxu\AppData\Local\Programs\Python\Python311\python.exe

```

#### 有时候有一些包，我们使用uv sync不好使，还是下载不下来。那就得手动下载到本地，然后执行

```
uv pip install C:\Users\jinxu\Downloads\pyicu-2.15.3-cp311-cp311-win_amd64.whl --force-reinstall --no-index
```

这样执行uv pip就安装到.venv里了。

如果还是不行，就修改pyproject.toml,增加下面代码：

```

[tool.uv.sources]
pyicu = { path = "C:/Users/jinxu/Downloads/pyicu-2.16-cp311-cp311-win_amd64.whl" }
```

修改source指向本地的包，然后在执行

```
uv clean 
uv sync
```

#### 启动

 有时候一些开源项目，他的main不在最外面。那么启动就要用这种模式

```
python -m api.ragflow_server
```

`-m` 会把当前目录加入 `sys.path`。

Python 启动时，`sys.path` 会包含：

1. **当前脚本所在目录**（或者执行 `-m` 时的模块所在目录）。
2. **环境变量 PYTHONPATH** 指定的路径。
3. **标准库路径**，比如 `C:\Python310\Lib`。
4. **已安装的 site-packages 目录**。

如下图，这样启动就会把common文件夹载入。

![1762927266345](C:\GitHub\kiba_py_uv\README.assets\1762927266345.png)

运行时，会下载hugface，也就是说，运行时要挂vpn。

运行时还缺nltk的包，找文件添加下面代码，添加到ragflow_server.py可能更好。

```
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
```

![1762929327197](C:\GitHub\kiba_py_uv\README.assets\1762929327197.png)

启动成功后，删除这个代码即可。

出现logo就是启动成功了。

![1762929434273](C:\GitHub\kiba_py_uv\README.assets\1762929434273.png)

ragflow的依赖环境还是要用dockerdesktop安装的。启动api要把docker里的api停了，不然端口冲突。

![1762929472978](C:\GitHub\kiba_py_uv\README.assets\1762929472978.png)

【使用python配置启动ragflow】这样就可以调试了

![1763004532556](C:\GitHub\kiba_py_uv\README.assets\1763004532556.png)

## 代码编写介绍
在文件夹下，增加init.py文件，能把该文件夹变成模块。

init.py里什么都不写也可以。

![1763014450786](C:\GitHub\kiba_py_uv\README.assets\1763014450786.png)

变成模块后，我们就可以选择模块启动方式了。

 ![1763014558757](C:\GitHub\kiba_py_uv\README.assets\1763014558757.png)


## requirements
requirements是使用uv命令导出的，因为把python代码在docker里运行的时候，需要安装依赖，docker容器有pip，但没有uv。
因为uv的安装比较费劲，所以直接用uv命令导出requirements，这样就在制造dockerfile的时候，可以直接pip requirements安装依赖了。
uv export --format=requirements.txt --output-file=requirements.txt

![1764309010259](C:\GitHub\kiba_py_uv\README.assets\1764309010259.png)