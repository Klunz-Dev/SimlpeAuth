from fastapi import FastAPI, HTTPException
from schemes import *
from dep import SessionDep
from model import UserModel
from hashing import hash_password
from jwt_token_config import *

app = FastAPI(title='SimpleAuth')

@app.get('/', tags=['system'], summary='base information')
async def base_endpoint():
    return 'Welcome to SimpleAuth'

@app.post('/create_account', tags=['user'], summary='User create new account')
async def create_account(creds: CreateUser, session: SessionDep):
    try:
        password, salt = hash_password(password=creds.password)

        new_user = UserModel(
            first_name = creds.first_name,
            username = creds.username,
            bio = creds.bio,
            mail = creds.mail,
            hash_password = password,
            salt = salt
        )
    
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        access_token = auth.create_access_token(uid=new_user.username)
        user_id = new_user.id
        username = new_user.username

        return{'access token': access_token,
               'user_id': user_id,
               'username': username}

    except Exception as e:
        return e

@app.get('/get_account/{user_id}', tags=['user'], summary='Get user account (user_id)')
async def get_account(user_id: int):
    ...

@app.put('/update_account/{user_id}', tags=['user'], summary='Update data account (user_id)')
async def update_account(user_id: int):
    ...

@app.put('/delete_account/{user_id}', tags=['user'], summary='Delete account (user_id)')
async def delete_account():
    ...
