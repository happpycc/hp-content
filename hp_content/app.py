from aiohttp import web
from handle import app as handle_app
from settings import HOST, PORT

app = web.Application()
app.add_subapp("/api/content", handle_app)


if __name__ == "__main__":
    web.run_app(app, host=HOST, port=PORT)
