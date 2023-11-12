import pytest
import os
from app.db.session import SessionLocal, engine, SQLALCHEMY_DATABASE_URL
from app.db.models.item import ItemModel
from app.db.connection import get_db

@pytest.fixture(scope="module", autouse=True)
def app():
    # 환경 변수
    print(f'\n{SQLALCHEMY_DATABASE_URL=}')
    if "5342" in SQLALCHEMY_DATABASE_URL: # public db
        raise ValueError("실제 DB에 테이블을 생성할 수 없습니다")
    # items 테이블 없으면 생성
    ItemModel.__table__.create(engine, checkfirst=True)
    yield
    

@pytest.fixture(scope="function", autouse=True)
def session():
    db = next(get_db())
    db.query(ItemModel).delete()
    db.commit()
    db_item = ItemModel(id=1, name="John", content="This is a test code.")
    db.add(db_item)
    db.commit()
    yield

