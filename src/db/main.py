from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

async_engine = AsyncEngine(
    create_engine(
        url="postgresql+asyncpg://postgres:%21%40%23DreamOnline123@localhost:5432/bookly_dev_db",
        echo=True
    )
)

async def init_db() -> None:
    async with async_engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with session() as session:
        yield session
