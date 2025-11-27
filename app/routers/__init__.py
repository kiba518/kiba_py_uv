# app/routers/__init__.py

from fastapi import APIRouter

# 导入所有子路由文件中的 router 对象
# 注意：这里我们直接从文件导入 router 对象
from .test.items import router_items
from .test.api_test import router_api_test
from .mcp.sse import router_sse

# 创建一个顶层 APIRouter 实例
# api_router = APIRouter() 这种不加参数就是创建顶级的路由，都将直接基于应用程序的根路径 /
api_router = APIRouter()

# 包含所有子路由
api_router.include_router(router_items)
api_router.include_router(router_api_test)
api_router.include_router(router_sse)

# 注意：当其他文件导入 app.routers 时，它们会自动获得 api_router 对象
# 这就是 __init__.py 的作用