from fastapi import Request
from fastapi.responses import JSONResponse


class UserAlreadyExists(Exception):
    pass


class UserNotFound(Exception):
    pass


class InvalidPassword(Exception):
    pass


async def user_already_exists_handler(request: Request, exc: UserAlreadyExists):
    return JSONResponse(status_code=409, content={"detail": str(exc)})


async def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def invalid_password_handler(request: Request, exc: InvalidPassword):
    return JSONResponse(status_code=401, content={"detail": str(exc)})
