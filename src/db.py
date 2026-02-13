from .model import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

db_url = 'sqlite+aiosqlite:///name_data_base.db'
async_engine = create_async_engine(url=db_url)
async_session = async_sessionmaker(bind=async_engine)

async def get_session():
    async with async_session as session:
        yield session

async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        
