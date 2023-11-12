import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# from .models import *

DATABASE_URL = f"postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/MKHOST"

Base = declarative_base()

connect_args = {"server_settings": {"options": "-c timezone=UTC", "timezone": "UTC"}}
engine = create_async_engine(DATABASE_URL, future=True, connect_args=connect_args)

async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# TODO: following functions would be removed in the future.
async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
        await session.commit()
