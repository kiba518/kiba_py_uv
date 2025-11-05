from sqlalchemy.orm import Session
from app.tables.items import models


def get_items(db: Session):
    return db.query(models.Item).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, name: str, description: str):
    new_item = models.Item(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id: int, name: str, description: str):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        item.name = name
        item.description = description
        db.commit()
        db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
