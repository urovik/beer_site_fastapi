from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


from app.user import router as router_users
from app.api_rq import router as api_router
from app.auth.jwt import router as jwt_router    
from src.database.models import db_init

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app:FastAPI):
    await db_init()
    yield

app = FastAPI(title = "api_for_beer",lifespan = lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router = router_users)
app.include_router(router = api_router)
app.include_router(router= jwt_router)



if __name__ == '__main__':
    uvicorn.run("main:app", reload = True)