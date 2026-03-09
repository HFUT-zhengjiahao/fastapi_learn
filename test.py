from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel,Field
class user(BaseModel):
    username:str = Field(default="张栩")
    full_name:str = Field(...)
@app.get('/users/')
def create_user(user:user):
    return user