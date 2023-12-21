from fastapi import FastAPI

from routers import models

app = FastAPI()
app.include_router(models.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
