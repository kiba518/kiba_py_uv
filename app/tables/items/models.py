from sqlalchemy import Column, Integer, String
from app.database import Base, engine



class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))

Base.metadata.create_all(bind=engine) # 自动建表