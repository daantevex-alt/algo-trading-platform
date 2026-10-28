from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.db.session import session_factory
from app.db.unit_of_work import UnitOfWork
from app.repositories.user_repositories import UserRepository
from app.repositories.StrategyRepositories import StrategyRepository
from app.services.User_service import UserService
from app.services.strategy_service import StrategyService
from app.core.redis import client


async def get_session() -> AsyncSession:
    async with session_factory() as session:
        yield session


async def get_unit_of_work(
    session: AsyncSession = Depends(get_session),
) -> UnitOfWork:
    return UnitOfWork(session)


async def get_user_service(
    unit_of_work: UnitOfWork = Depends(get_unit_of_work),
) -> UserService:
    return UserService(unit_of_work=unit_of_work)


async def get_strategy_repository(
    session: AsyncSession = Depends(get_session),
) -> StrategyRepository:
    return StrategyRepository(session)


async def get_strategy_service(
    repository: StrategyRepository = Depends(get_strategy_repository),
) -> StrategyService:
    return StrategyService(repository, client)
