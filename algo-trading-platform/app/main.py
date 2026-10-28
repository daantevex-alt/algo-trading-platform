from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.session import create_tables
from app.api import users, strategies
from app.exceptions.user import (
    UserAlreadyExists,
    UserNotFound,
    InvalidPassword,
    user_already_exists_handler,
    user_not_found_handler,
    invalid_password_handler,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Algo Trading Platform",
    description="REST API для управления алгоритмическими торговыми стратегиями",
    version="0.1.0",
    lifespan=lifespan,
)


app.include_router(users.router)
app.include_router(strategies.router)

app.add_exception_handler(UserAlreadyExists, user_already_exists_handler)
app.add_exception_handler(UserNotFound, user_not_found_handler)
app.add_exception_handler(InvalidPassword, invalid_password_handler)


@app.get("/health", tags=["system"])
async def health_check():
    return {"status": "ok"}
