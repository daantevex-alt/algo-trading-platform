from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repositories import UserRepository
from app.repositories.StrategyRepositories import StrategyRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repository = UserRepository(session)
        self.strategy_repository = StrategyRepository(session)

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, traceback):
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                await self.session.rollback()
        except Exception:
            await self.session.rollback()
            raise
