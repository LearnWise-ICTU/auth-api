from config.config import Settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI
from fastapi import FastAPI


from database.mongod import init_db, close_db

from routes.v1 import users


app = FastAPI(
    title=Settings().APP_NAME,
    version=Settings().APP_VERSION,
    description=Settings().APP_DESCRIPTION,
)


# add routers
app.include_router(users.router)


app = VersionedFastAPI(
    app, enable_latest=True, version_format="{major}", prefix_format="/v{major}"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


async def startup():
    print("Starting up")
    await init_db(app)


async def shutdown():
    print("Shutting down")
    await close_db(app)


app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)


@app.get("/healthcheck")
def api_healthcheck():
    return "OK 200 - app running successfully"


# # register routers
# app.include_router(course.router)
