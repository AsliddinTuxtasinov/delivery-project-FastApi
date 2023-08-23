from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
async def index():
    return {"message": "Yahoo, Hello World"}
