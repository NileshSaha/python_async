import uvicorn
from fastapi import FastAPI

from src.db.config import engine, Base
from src.routers import index

app = FastAPI()
app.include_router(index.baseRouter)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup():
    await init_db()


if __name__ == '__main__':
    uvicorn.run("app:app", port=8000, host='127.0.0.1')
