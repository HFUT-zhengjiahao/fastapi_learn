from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel,Field,field_validator

class user(BaseModel):
    username:str = Field(default="张栩")
    full_name:str = Field(...)

class account(BaseModel):
    username:str = Field(default="张栩")
    password:str = Field(...,pattern="^\\w{6,}$",max_length=10,title="密码",description="密码长度不能超过10位",examples=["123456"])
@app.get('/users/')
def create_user(user:user):
    return user

#接收用户提交的数据
@app.post('/accounts/')
def create_account(account:account):
    return account

#自定义验证
class Users2(BaseModel):
    email:str = Field()

    #可以随意添加规则
    @field_validator('email')
    def check_email(cls,value):    #名字无所谓，只要上面有@就好
        if "@" not in value:
            raise ValueError("邮箱格式错误")
        return value
    
@app.post('/users2/')
def create_user2(user:Users2):
    return user


#case:传递多个信息
class order(BaseModel):
    items:list = Field(...,min_items=1,max_items=10)
    address:str = Field(...,description="地址")

@app.post('/orders/')
def create_order(order:order):
    return order


#枚举型
from enum import Enum
class Stutas(str,Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class Item(BaseModel):
    name:str
    status:Stutas = Field(default=Stutas.PENDING)

@app.post('/items/')
def create_item(item:Item):
    return item