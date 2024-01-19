import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, Request
from envparse import Env
from fastapi.routing import APIRouter, APIRoute

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/test_database")

async def ping() -> dict:
    return {"Success": True}

async def mainpage() -> str:
    return "YOU ARE ON THE MAIN PAGE"

async def create_record(request: Request) -> dict:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["test_database"]
    await mongo_client.records.insert_one({"sample": "record!!!!"})
    return {"Success": True}

async def get_record(rrequest: Request) -> list:
    mongo_client: AsyncIOMotorClient = rrequest.app.state.mongo_client["test_database"]
    cursor = mongo_client.records.find({})
    res = []
    for document in await cursor.to_list(length=100):
        document["_id"] = str(document["_id"])
        res.append(document)
    return res

routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/", endpoint=mainpage, methods=["GET"]),
    APIRoute(path="/create_record", endpoint=create_record, methods=["POST"]),
    APIRoute(path="/get_record", endpoint=get_record, methods=["GET"]),
]
client = AsyncIOMotorClient(MONGODB_URL)
app = FastAPI()
app.state.mongo_client = client
app.include_router(APIRouter(routes=routes))

# {if __name__ == "5_1":}
#uvicorn.run(app, host="0.0.0.0", port=8000)