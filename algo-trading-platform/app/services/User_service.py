from app.core.security import verify_password, hash_password
from app.db.unit_of_work import UnitOfWork
from app.exceptions.user import UserNotFound, UserAlreadyExists, InvalidPassword
from app.models.model import User
from app.schemas.user import UserCreate, UserLogin, UserResponse


class UserService:
    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    async def register_user(self, user: UserCreate) -> UserResponse:
        async with self.unit_of_work:
            existing_user = await self.unit_of_work.user_repository.get_by_email(user.email)
            if existing_user:
                raise UserAlreadyExists(f"User with email {user.email} already exists")

            hashed_password = hash_password(user.password)

            new_user = User(
                email=user.email,
                password=hashed_password,
                age=user.age,
                username=user.username,
            )

            saved_user = await self.unit_of_work.user_repository.create(new_user)
            return UserResponse.model_validate(saved_user)

    async def login_user(self, user: UserLogin) -> UserResponse:
        async with self.unit_of_work:
            found_user = await self.unit_of_work.user_repository.get_by_email(user.email)
            if not found_user:
                raise UserNotFound(f"User with email {user.email} not found")

            if not verify_password(user.password, found_user.password):
                raise InvalidPassword("Invalid password")

            return UserResponse.model_validate(found_user)
