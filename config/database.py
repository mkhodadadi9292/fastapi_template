import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from . import api_router
from .exceptions import setup_custom_errors
from database.database import create_all, DATABASE_URL
print("Creating")
print("================================================")
print(DATABASE_URL)
print("================================================")
print("Creating")
#########################################
# from ..mock.init_database import init_database
# from .scheduler import scheduler
########################################
origins = [
    "*"
]


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}_{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
app.include_router(api_router.api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
setup_custom_errors(app)


@app.on_event("startup")
async def startup():
    # await create_all()
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
