from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from config.config import Settings
from beanie import init_beanie
from fastapi import FastAPI


# models
from models.user import User


documents = [User]


async def init_db(app: FastAPI):

    # Create a new client and connect to the server
    app.mongodb_client = AsyncIOMotorClient(
        Settings().MONGODB_URL, server_api=ServerApi("1")
    )
    # Send a ping to confirm a successful connection
    database = app.mongodb_client[Settings().DATABASE_NAME]
    try:
        await init_beanie(database=database, document_models=documents)
        app.mongodb_client.admin.command("ping")
        print("You successfully connected to Database!")
    except Exception as e:
        print(e)
        print("Database Not Connected!")


async def close_db(app: FastAPI):
    app.mongodb_client.close()
    print("Database Connection Closed!")
