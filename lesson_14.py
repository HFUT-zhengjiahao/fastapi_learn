#文件上传1
#pip install aiofiles
from fastapi import FastAPI,File,UploadFile
import aiofiles

app = FastAPI()

""" 1. 使用File上传文件 """
#小文件无需异步
@app.post("/upload/")
def upload_file1(file:bytes=File(...)):
    with open("./data/file.png", "wb") as f:   #注意这里需要自己创建data文件夹，否则会报错
        f.write(file)
    return {"msg":"上传成功"}

""" 2. 使用UploadFile上传文件 """
@app.post("/upload2/")
async def upload_file2(file:UploadFile=File(...)):
    async with aiofiles.open(f"./data/{file.filename}", "wb") as f:
        # chunk = await file.read(1024*1024)
        # while chunk:
        #     await f.write(chunk)
        #     chunk = await file.read(1024*1024)
        #下面是简化写法
        while chunk := await file.read(1024*1024):
            await f.write(chunk)
    return {"msg":"上传成功"}
