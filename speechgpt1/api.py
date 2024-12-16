import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
     return {"greeting":"Hello world"}

@app.get("/info")
async def get_info():
    return {"aboba": "true"}
