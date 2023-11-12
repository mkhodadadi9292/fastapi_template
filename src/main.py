from fastapi.routing import APIRoute
from fastapi import FastAPI, APIRouter
from src.app1 import apps as app1
from src.app2 import apps as app2


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}_{route.name}"


# Add each router in each app to app.include_routers.
app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
app.include_router(app1.router)
app.include_router(app2.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
