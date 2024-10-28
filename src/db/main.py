from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os
from src.config import DatabaseConfig

# load_dotenv()
#
# DATABASE_URL = os.getenv('DATABASE_URL')

async_engine = AsyncEngine(
    create_engine(
        url=DatabaseConfig.DATABASE_URL,
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
