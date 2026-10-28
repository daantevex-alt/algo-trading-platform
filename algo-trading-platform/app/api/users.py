from fastapi import APIRouter, Depends

from app.dependencies import get_user_service
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.User_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    user_create: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    return await user_service.register_user(user=user_create)


@router.post("/login", response_model=UserResponse)
async def login(
    user_login: UserLogin,
    user_service: UserService = Depends(get_user_service),
):

    return await user_service.login_user(user=user_login)
