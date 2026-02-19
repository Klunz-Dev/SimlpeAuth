from model import *
from sqlalchemy import select
from sqlalchemy.exc import IdentifierError
from server import HTTPException
from schemes import *
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

db_url = 'sqlite+aiosqlite:///users.db'
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
        
async def get_current_user(creds: CreateUser):
    async with async_session as session:
        existing_user = await session.execute(
            select(UserModel).where(
                (UserModel.username == creds.username) |
                (UserModel.mail == creds.mail)
            )
        )

        current_user = existing_user.scalars().first()

        if current_user:
            if current_user.username == creds.username:
                raise HTTPException(status_code=400, detail='Error, username already')
            
            if current_user.mail == creds.mail:
                raise HTTPException(status_code=400, detail='Error, mail already')