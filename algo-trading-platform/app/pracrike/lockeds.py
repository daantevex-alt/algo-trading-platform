from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, ForeignKey


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("app_users.id"), nullable=False)
    status: Mapped[str] = mapped_column(nullable=False, default="pending")


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_pending_task(self) -> Task | None:
        stmt = (
            select(Task)
            .where(Task.status == "pending")
            .order_by(Task.id)
            .limit(1)
            .with_for_update(skip_locked=True)
        )
        result = await self.session.execute(stmt)
        task = result.scalar_one_or_none()

        if task is None:
            return None

        task.status = "processing"
        await self.session.flush()
        return task

    async def create(self, task: Task) -> Task:
        self.session.add(task)
        await self.session.flush()
        return task
