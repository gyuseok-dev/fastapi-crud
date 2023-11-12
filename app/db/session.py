from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # Base 생성
# from core.config import settings
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

import os

DB_URL = name = os.getenv("DATABASE_URL", "postgresql://postgres:test1234@localhost:5432/postgres")
if not DB_URL:
    # error 발생
    raise ValueError("올바르지 않은 DATABASE_URL 입니다.")

# PostgreSQL 연결 설정
SQLALCHEMY_DATABASE_URL = DB_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()