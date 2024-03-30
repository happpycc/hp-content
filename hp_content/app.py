from aiohttp import web
from handle import app as handle_app
from motor.motor_asyncio import AsyncIOMotorClient
from settings import DB_HOST, DB_PORT, SERVER_HOST, SERVER_PORT

app = web.Application()
db = AsyncIOMotorClient(DB_HOST, DB_PORT)
app["db"] = db["hp-content"]
handle_app["db"] = app["db"]
app.add_subapp("/api/content", handle_app)


if __name__ == "__main__":
    web.run_app(app, host=SERVER_HOST, port=SERVER_PORT)
