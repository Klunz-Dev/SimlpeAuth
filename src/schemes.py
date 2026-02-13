from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    username: str = Field(..., title="You'r username", min_length=1, max_length=16)
    bio: str = Field(..., title="You'r bio (min: 128, max: 512)", min_length=1, max_length=512)
    mail: EmailStr
    password: str = Field(..., title="You'r password (min: 8, max: 32)", min_length=8, max_length=32)

class ReadUser(CreateUser):
    id: int
    username: str
    bio: str
    mail: EmailStr

class UpdateUser():
    username: str = Field(None, title="You'r new username", min_length=1, max_length=16)
    bio: str = Field(None, title="You'r new bio", min_length=1, max_length=512)
    mail: EmailStr = Field(None, title="You'r new mail")

class DeleteUser():
    id: int