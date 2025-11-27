from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.tables.items import crud

router_items = APIRouter(prefix="/items", tags=["操作item表信息"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router_items.get("/")
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router_items.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item(db, item_id)

@router_items.post("/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    return crud.create_item(db, name, description)

@router_items.put("/{item_id}")
def update_item(item_id: int, name: str, description: str, db: Session = Depends(get_db)):
    return crud.update_item(db, item_id, name, description)

@router_items.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)
