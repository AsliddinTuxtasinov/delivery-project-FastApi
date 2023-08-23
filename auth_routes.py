from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
async def sign_up():
    return {"message": "It is auth rote api"}
