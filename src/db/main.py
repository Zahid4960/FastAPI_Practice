from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from src.config import Config

engine: AsyncEngine = create_async_engine(
        url="postgresql+asyncpg://postgres:%21%40%23DreamOnline123@localhost:5432/bookly_dev_db",
        echo=True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    print("Tables created successfully")

# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         bind=engine, class_=AsyncSession, expire_on_commit=False
#     )
#
#     async with async_session() as session:
#         yield session
