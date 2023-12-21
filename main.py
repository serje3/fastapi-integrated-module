from fastapi import FastAPI

from routers import datasets

app = FastAPI()
app.include_router(datasets.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

