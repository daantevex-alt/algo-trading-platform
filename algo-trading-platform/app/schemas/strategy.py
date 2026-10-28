from pydantic import BaseModel


class StrategyResponse(BaseModel):
    id: int
    name: str
    description: str | None
    strategy_type: str
    budget: float | None
    is_active: bool
    user_id: int

    model_config = {"from_attributes": True}


class StrategyCreate(BaseModel):
    name: str
    description: str | None = None
    strategy_type: str
    budget: float | None = None
