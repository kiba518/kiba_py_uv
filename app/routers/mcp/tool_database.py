import json
from app.database import SessionLocal
from app.tables.items import crud
from . import mcp
from fastapi.encoders import jsonable_encoder

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 工具里不能用依赖 db: Session = Depends(get_db)
@mcp.tool()
async def get_item() -> str:
    """获取数据库 item表数据.
     Args:无
     """
    print("执行调用get_item")
    db = next(get_db())
    items = crud.get_items(db)

    # ORM 对象 → 可 JSON 的 dict
    items_dict = jsonable_encoder(items)
    # 转成 JSON 字符串
    return json.dumps(items_dict, ensure_ascii=False, indent=2)





if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="sse")
