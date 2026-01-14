
from fastapi import FastAPI
from app.db.database import engine, Base
from app.routers.item_router import router as item_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Inventory Management API", version="1.0.0", lifespan=lifespan)

app.include_router(item_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Inventory Management API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
