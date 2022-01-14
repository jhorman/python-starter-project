from fastapi import APIRouter

status_router = APIRouter()


@status_router.get("/")
async def status():
    return {"status": "OK"}
