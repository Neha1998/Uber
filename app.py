import uvicorn
from fastapi import FastAPI

from Uber.User.views import user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)