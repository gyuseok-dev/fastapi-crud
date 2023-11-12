from sqlalchemy import Column, Integer, String, DateTime, Text, func
from db.session import Base

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String)
    content = Column(Text)