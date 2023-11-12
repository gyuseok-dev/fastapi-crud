from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_URL = name = os.getenv("DATABASE_URL")
IS_CONTAINER = os.getenv("IS_CONTAINER", "false")

if not DB_URL and IS_CONTAINER == "true":
    # error 발생
    raise ValueError("올바르지 않은 DATABASE_URL 입니다.")
TEST_DB_URL = name = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:test1234@localhost:5433/postgres")

# PostgreSQL 연결 설정
if DB_URL and IS_CONTAINER == "true":
    SQLALCHEMY_DATABASE_URL = DB_URL
else:
    SQLALCHEMY_DATABASE_URL = TEST_DB_URL
print(f'{SQLALCHEMY_DATABASE_URL=}')
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()