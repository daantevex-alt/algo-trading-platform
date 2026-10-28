from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.model import Strategy


class StrategyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, strategy_id: int) -> Strategy | None:
        stmt = select(Strategy).where(Strategy.id == strategy_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all_by_user(self, user_id: int) -> list[Strategy]:
        stmt = select(Strategy).where(Strategy.user_id == user_id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def create(self, strategy: Strategy) -> Strategy:
        self.session.add(strategy)
        await self.session.flush()
        return strategy
