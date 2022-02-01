import uvicorn
from fastapi import FastAPI

from Uber.User.views import user_router
from Uber.Vehicle.views import vehicle_router
from Uber.ride.views import ride_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Uber!!"}


app.include_router(user_router)
app.include_router(vehicle_router)
app.include_router(ride_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)