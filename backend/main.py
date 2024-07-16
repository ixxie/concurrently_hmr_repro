import uvicorn
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.basicConfig(encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger("backend")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
def hello(name: str):
    logger.info(f"running hello {name}")
    return {"Hello": name}


@app.get("/goodbye")
def goodbye():
    logger.warning("running goodbye")
    raise Exception("GOODBYE")
    return {"Goodbye": "World"}


@app.get("/async_goodbye")
async def goodbye():
    loop = asyncio.get_event_loop()

    async def say_goodbye():
        logger.warning("running asunc goodbye")
        raise Exception("ASYNC GOODBYE")
        return "nope"

    loop.create_task(say_goodbye())
    return {"Goodbye": "World"}


def run():
    """main entry point"""
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
