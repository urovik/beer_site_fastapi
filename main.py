from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

from database.models import db_init
from users.router import router as router_users
from auth.router import router as jwt_router
from products.router import router as products_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    await db_init()
    yield

app = FastAPI(title = "api_for_beer",lifespan = lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router_users)
app.include_router(router=jwt_router)
app.include_router(router=products_router)



if __name__ == '__main__':
    uvicorn.run("main:app", reload = True)