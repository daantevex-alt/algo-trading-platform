import json

from fastapi import HTTPException, status

from app.repositories.StrategyRepositories import StrategyRepository
from app.schemas.strategy import StrategyResponse


class StrategyService:

    def __init__(self, repository: StrategyRepository, redis):
        self.repository = repository
        self.redis = redis

    async def get_strategy(self, strategy_id: int) -> StrategyResponse:
        key = f"strategy:{strategy_id}"

        cached = await self.redis.get(key)
        if cached is not None:
            return StrategyResponse(**json.loads(cached))

        strategy = await self.repository.get_by_id(strategy_id)
        if strategy is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Strategy with id {strategy_id} not found",
            )

        response = StrategyResponse.model_validate(strategy)
        await self.redis.set(key, response.model_dump_json(), ex=60)
        return response
