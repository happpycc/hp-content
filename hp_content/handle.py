import re
from datetime import datetime

from aiohttp import web
from bson import json_util
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

app = web.Application()
route = web.RouteTableDef()


def verify_path(path) -> bool:
    pattern = re.compile(r"^(/[a-zA-Z0-9]+)+$")
    if type(path) != str:
        return False
    if path == "":
        return False
    if not pattern.match(path):
        return False
    return True


def verify_text(text) -> bool:
    if type(text) != dict:
        return False
    return True


def verify_collection(collection) -> bool:
    pattern = re.compile(r"^(?!system\.)[^\0]+$")
    if len(collection) >= 120:
        return False
    if not pattern.match(collection):
        return False
    return True


@route.get("/id/{collection}/{_id}")
async def query_content_by_id(request: web.Request):
    collection: str = request.match_info["collection"]
    _id: str = request.match_info["_id"]
    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})
    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].find_one({"_id": ObjectId(_id)})
    print(result)
    return web.json_response({"route": "get_task_by_id"})


@route.get("/path/{collection}/{path:.*}")
async def query_content_by_path(request: web.Request):
    collection: str = request.match_info["collection"]
    path: str = "/" + request.match_info["path"]
    print(path)
    db: AsyncIOMotorDatabase = request.app["db"]
    if path == "":
        result = await db[collection].find()
        return web.json_response(result)
    if not verify_collection(collection) or not verify_path(path):
        return web.json_response({"code": 1, "error": "Data Format Error."})
    result = await db[collection].find({"path": path}).to_list(length=None)
    return web.json_response(text=json_util.dumps(result))


@route.get("/collection/{collection}")
async def query_content_by_id(request: web.Request):
    collection: str = request.match_info["collection"]
    db: AsyncIOMotorDatabase = request.app["db"]
    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})
    result = await db[collection].find().to_list(length=None)
    return web.json_response(text=json_util.dumps(result))


@route.post("/{collection}")
async def add_content(request: web.Request):
    collection: str = request.match_info.get("collection")
    data = await request.json()
    if (
        not verify_path(data["path"])
        or not verify_text(data["text"])
        or not verify_collection(collection)
    ):
        return web.json_response({"code": 1, "error": "Data Format Error."})
    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].insert_one(
        {
            "text": data["text"],
            "path": data["path"],
            "create_time": datetime.now(),
            "update_time": datetime.now(),
        }
    )
    print(result)
    return web.json_response({"code": 0, "result": "Added Successfully."})


@route.put("/text/{collection}/{_id}")
async def update_content_by_id(request: web.Request):
    collection: str = request.match_info["collection"]
    _id: str = request.match_info["_id"]
    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    data = await request.json()
    text = data["text"]
    if not verify_text(text):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].update_one(
        {"_id": ObjectId(_id)}, {"$set": {"text": text, "update_time": datetime.now()}}
    )
    print(result)
    return web.json_response({"code": "0", "result": "Uploaded Successfully."})


@route.put("/path/{collection}/{_id}")
async def update_content_by_id(request: web.Request):
    collection: str = request.match_info["collection"]
    _id: str = request.match_info["_id"]
    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    data = await request.json()
    path = data["path"]
    if not verify_path(path):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].update_one(
        {"_id": ObjectId(_id)}, {"$set": {"path": path, "update_time": datetime.now()}}
    )
    print(result)
    return web.json_response({"code": "0", "result": "Uploaded Successfully."})


@route.delete("/id/{collection}/{_id}")
async def delete_content_by_id(request: web.Request):
    collection: str = request.match_info["collection"]
    _id: str = request.match_info["_id"]

    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].delete_one({"_id": ObjectId(_id)})
    print(result)
    return web.json_response({"code": "0", "result": "Deleted Successfully."})


@route.delete("/path/{collection}/{path:.*}")
async def delete_content_by_path(request: web.Request):
    collection: str = request.match_info["collection"]
    path: str = "/" + request.match_info["path"]

    if not verify_collection(collection) or not verify_path(path):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db[collection].delete_many({"path": path})
    print(result)
    return web.json_response({"code": "0", "result": "Deleted Successfully."})


@route.delete("/collection/{collection}")
async def delete_collection(request: web.Request):
    collection: str = request.match_info["collection"]

    if not verify_collection(collection):
        return web.json_response({"code": 1, "error": "Data Format Error."})

    db: AsyncIOMotorDatabase = request.app["db"]
    result = await db.drop_collection(collection)
    print(result)
    return web.json_response({"code": "0", "result": "Deleted Successfully."})


app.add_routes(route)
