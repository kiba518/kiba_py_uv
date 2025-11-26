## MCP SSE
直接运行server，右键直接运行即可。
```
C:\GitHub\kiba_py_uv\.venv\Scripts\python.exe C:\GitHub\kiba_py_uv\mcp\server.py 
```
#### 依赖
项目在原来的基础上增加了:
```
    "httpx>=0.28.1",
    "fastmcp>=2.13.1",
```


## 什么是 MCP？

[模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 是一个开放标准，使 AI 模型能够与外部工具和数据源交互。MCP 解决了 AI 开发中的几个关键挑战：

- **上下文限制**：允许模型访问超出其训练数据的最新信息
- **工具集成**：为模型使用外部工具和 API 提供标准化方式
- **互操作性**：在不同 AI 模型和工具之间创建通用接口
- **可扩展性**：便于在无需重新训练的情况下为 AI 系统添加新功能

本项目展示了如何在 FastAPI Web 应用中使用服务器推送事件 (SSE) 实现 MCP。

## 描述

本项目展示了如何使用 FastAPI 框架实现服务器推送事件 (SSE)，同时集成模型上下文协议 (MCP) 功能。其核心特点是将 MCP 的 SSE 功能无缝集成到一个包含自定义路由的完整 FastAPI Web 应用中。

## 功能

- 基于 MCP 的服务器推送事件 (SSE) 实现
- 与 FastAPI 框架集成，支持自定义路由
- 统一 Web 应用，同时支持 MCP 和标准 Web 端点
- 可自定义的路由结构
- MCP 功能与 Web 功能的清晰分离

## 架构

本项目展示了一个模块化架构，包括：

1. 将 MCP SSE 端点（`/sse` 和 `/messages/`）集成到 FastAPI 应用中
2. 提供标准 Web 路由（`/`、`/about`、`/status`、`/docs`, `/redoc`）
3. 展示如何保持 MCP 功能与 Web 路由的分离

### 可用端点

启动服务器后（使用选项 1 或选项 2），以下端点将可用：

- 主服务器：http://localhost:8000
- 标准 Web 路由：
  - 主页：http://localhost:8000/
  - 关于页面：http://localhost:8000/about
  - 状态 API：http://localhost:8000/status
  - 文档 (Swagger UI)：http://localhost:8000/docs
  - 文档 (ReDoc): http://localhost:8000/redoc
- MCP SSE 端点：
  - SSE 端点：http://localhost:8000/sse
  - 消息发布：http://localhost:8000/messages/

### 使用 MCP Inspector 调试

使用 MCP Inspector 测试和调试 MCP 功能：

```cmd
mcp dev ./src/weather.py
```

### 连接到 MCP Inspector

1. 打开 MCP Inspector：http://localhost:5173
2. 配置连接：
   - 设置传输类型为 `SSE`
   - 输入 URL：http://localhost:8000/sse
   - 点击 `Connect`

### 测试功能

1. 导航到 `Tools` 部分
2. 点击 `List Tools` 查看可用功能：
   - `get_alerts`：获取天气警报
   - `get_forecast`：获取天气预报
3. 选择一个功能
4. 输入所需参数
5. 点击 `Run Tool` 执行

## 扩展应用

### 添加自定义路由

应用结构便于使用 FastAPI 的 APIRouter 添加新路由：

1. 在 routes.py 中使用 APIRouter 定义新的路由处理程序：

   ```python
   @router.get("/new-route")
   async def new_route():
       return {"message": "这是一个新路由"}
   ```

2. 使用 router 定义的所有路由将自动包含到主应用中

### 自定义 MCP 集成

MCP SSE 功能通过以下方式在 server.py 中集成：

- 创建 SSE 传输
- 设置 SSE 处理程序
- 将 MCP 路由添加到 FastAPI 应用

## 与 [Continue](https://www.continue.dev/) 集成

要将此 MCP 服务器与 Continue VS Code 扩展一起使用，请在 Continue 设置中添加以下配置：

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "name": "weather",
          "type": "sse",
          "url": "http://localhost:8000/sse"
        }
      }
    ]
  }
}
```