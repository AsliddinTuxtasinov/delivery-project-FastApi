from fastapi import FastAPI

from auth_routes import auth_router
from order_routs import order_router

app = FastAPI(
    title="Delivery API",
    summary="API for managing delivery orders",
    description="This API allows you to manage delivery orders and authenticate users. "
                "It provides endpoints for user authentication and order management.",
    version="1.0.0",
    docs_url="/swagger",

    contact={
        "name": "Asliddin Tuxtasinov",
        "url": "https://github.com/AsliddinTuxtasinov",
        "email": "asliddintukhtasinov5@gmail.com",
        "phone": "+998903908839"
    },
)

app.include_router(router=auth_router, tags=["auth"])
app.include_router(router=order_router, tags=["order"])


@app.get(path="/")
async def index():
    return {"message": "Yahoo, Hello World"}
