import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
     return {"greeting":"Hello world"}

@app.get("/info")
async def get_info():
     try:
          from model import Model
          model = Model()
          return {"aboba": model.predict()}
     except Exception:
          return {"message": "error during request"}
