from fastapi import APIRouter, exceptions, status

from werkzeug.security import generate_password_hash

from db.database import session, engine
from schemas.userSchemas import SignUpModel
from db.models import User

session = session(bind=engine)
auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
async def sign_up():
    return {"message": "It is auth rote api"}


@auth_router.post(path="/signup", status_code=status.HTTP_201_CREATED)
async def signUp(user: SignUpModel):
    print(f"user: {user}")
    db_email = session.query(User).filter(User.email == user.email).first()
    db_username = session.query(User).filter(User.username == user.username).first()

    if db_email:
        return exceptions.HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "err_msg": "This email is already exist !!!"
            }
        )

    if db_username:
        return exceptions.HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "err_msg": "This username is already exist !!!"
            }
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(password=user.password),

        is_staff=user.is_staff,
        is_active=user.is_active
    )
    session.add(new_user)
    session.commit()

    return new_user
