from fastapi import APIRouter

order_router = APIRouter(prefix="/order")


@order_router.get("/")
async def orders():
    return {"message": "It is order rote api"}
