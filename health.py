from fastapi import APIRouter

health_router = APIRouter(prefix="/health")

@health_router.get(
    "",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
async def health() -> dict:
    print('1')
    y = sunc(3)
    print('2')
    await y
    return {
        "status": "online",
        "engine": "on",
    }

async def sunc(x):
    import time
    time.sleep(3)
    return x+1