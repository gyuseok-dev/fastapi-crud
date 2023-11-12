# fastapi-crud
fastapi crud
# 환경 구성
python version: 3.11.6

# 초기 세팅 

## 가상환경 설치
python3 -m venv .venv

## macOS/Linux에서 가상환경 활성화
source .venv/bin/activate

## dependency 설치
pip install -r requirements.txt

## local 실행
cd app
uvicorn main:app --reload

## api hit (curl)
curl http://localhost:8000

# Dockerize

## 빌드
docker build -t fastapi-app .

## 실행
docker run -d -p 8000:8000 fastapi-app

# DockerCompose

## 실행
docker-compose --env-file .env up

## 실행(백그라운드)
docker-compose -d --env-file .env up

## 삭제
docker-compose down

# swagger url
http://localhost:8000/docs