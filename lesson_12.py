#这节课是Fastapi表单数据
#pip install python-multipart
from fastapi import FastAPI,Form
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.post("/login1")
def login1(username:str=Form(...),password:str=Form(...)):
    return {"username":username,"password":password}
