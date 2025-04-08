from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


from users.router import router as router_users
from src.app.http.api_rq import router as api_router
from auth.router import router as jwt_router    
from src.database.models import db_init

from fastapi.middleware.cors import CORSMiddleware


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

app.include_router(router = router_users)
app.include_router(router = api_router)
app.include_router(router = jwt_router)



if __name__ == '__main__':
    uvicorn.run("main:app", reload = True)