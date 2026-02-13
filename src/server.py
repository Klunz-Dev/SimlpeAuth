from fastapi import FastAPI, HTTPException

app = FastAPI(title='SimpleAuth')

@app.get('/', tags=['system'], summary='base information')
async def base_endpoint():
    return 'Welcome to SimpleAuth'

@app.post('/create_account', tags=['user'], summary='User create new account')
async def create_account():
    ...

@app.get('/get_account/{user_id}', tags=['user'], summary='Get user account (user_id)')
async def get_account(user_id: int):
    ...

@app.put('/update_account/{user_id}', tags=['user'], summary='Update data account (user_id)')
async def update_account(user_id: int):
    ...

@app.put('/delete_account/{user_id}', tags=['user'])