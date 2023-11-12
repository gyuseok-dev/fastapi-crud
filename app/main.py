from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional 
from pydantic import BaseModel
from .db.session import engine
from .db.connection import get_db
from .db.models.item import ItemModel
from sqlalchemy.exc import ProgrammingError

# FastAPI 앱 설정
app = FastAPI(title="Backend API", version="1.0.0") 

# Pydantic 모델
class Item(BaseModel):
    id: Optional[int] = None
    created: Optional[datetime] = None
    name: str
    content: str

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    content: str

class ItemUpdate(BaseModel):
    name: str
    content: str

class MigrationResponse(BaseModel):
    message: str

@app.post("/migrate", description="DB 테이블 생성용 API", response_model=MigrationResponse)
def migrate():
    try: 
        ItemModel.__table__.create(engine)
    except ProgrammingError as e:
        if e.code == 'f405':
            return {"message": "이미 생성되었습니다."}
        raise e
        
    return {"message": "success"}

@app.post("/create", description="생성", response_model=Item)
def create_item(item: ItemCreate):
    db = next(get_db())
    db_item = ItemModel(name=item.name, content=item.content)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/read/{item_id}", description="조회", response_model=Item)
def read_item(item_id: int):
    db = next(get_db())
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="유효하지 않은 ID입니다.")
    return item

@app.put("/update/{item_id}", description='수정', response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    db = next(get_db())
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="유효하지 않은 ID입니다.")
    db_item.name = item.name
    db_item.content = item.content
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/delete/{item_id}", description='삭제', response_model=Item)
def delete_item(item_id: int):
    db = next(get_db())
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="유효하지 않은 ID입니다.")
    db.delete(db_item)
    db.commit()
    return db_item
