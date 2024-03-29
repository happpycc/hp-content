from aiohttp import web

app = web.Application()
route = web.RouteTableDef()


@route.get("/get/{content_id}")
async def get_content_by_id(request: web.Request):
    return web.json_response({"route": "get_task_by_id"})


@route.post("/add")
async def add_content(request: web.Request):
    return web.json_response({"route": "add_task"})


@route.put("/update/{content_id}")
async def update_content_by_id(request: web.Request):
    return web.json_response({"route": "upload_task_by_id"})


@route.delete("/delete/{content_id}")
async def delete_content_by_id(request: web.Request):
    return web.json_response({"route": "delete_task_by_id"})


@route.delete("/delete")
async def delete_all_content(request: web.Request):
    return web.json_response({"route": "delete_all_content"})


app.add_routes(route)
