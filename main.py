from fastapi import FastAPI
from router import router 
from contextlib import asynccontextmanager
from database import init_db
import sys
import logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

logging.basicConfig(
    format='%(asctime)s.%(msecs)05d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

app.include_router(router)
