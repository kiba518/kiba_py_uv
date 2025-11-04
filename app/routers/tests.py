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
