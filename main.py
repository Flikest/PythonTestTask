from fastapi import FastAPI

from routes.userRouter import router


app = FastAPI()

app.include_router(router)