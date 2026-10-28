from fastapi import APIRouter, Depends

from app.dependencies import get_strategy_service
from app.schemas.strategy import StrategyResponse
from app.services.strategy_service import StrategyService

router = APIRouter(prefix="/strategies", tags=["strategies"])


@router.get("/{strategy_id}", response_model=StrategyResponse)
async def get_strategy(
    strategy_id: int,
    strategy_service: StrategyService = Depends(get_strategy_service),
):
    return await strategy_service.get_strategy(strategy_id)
