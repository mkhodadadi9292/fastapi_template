from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession

engine = create_engine(
    f"postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/MKHOST",
    echo=True
)

from sqlalchemy.future import select


async def run():
    async with AsyncSession(engine) as session:
        print("Executing")
        tr = 1
        # Execute your queries here
        # await session.execute(select("*").from_("users"))
        query_results = await session.execute(
            select('Users'))
        result = query_results.scalars().first()
        session.commit()
        return result
t = await run()
