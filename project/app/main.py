from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.api.user import router as user_router

app = FastAPI()
app.include_router(user_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()