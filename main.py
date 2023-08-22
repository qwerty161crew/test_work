import asyncio
import time

from fastapi import FastAPI

from models import TestResponse

app = FastAPI()


async def work(seconds) -> None:
    await asyncio.sleep(seconds)


@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    start_at = time.time()
    ts1 = await work(3)
    ts2 = await work(3)
    end_time = time.time()
    return TestResponse(elapsed=end_time - start_at)
