from fastapi import FastAPI

from server.middleware import middleware_init
from server.routers import router_init
from server.logs import log_init, sys_log
from server.mydbs.database import db_init
from server.utils.common_util import write_log


def con_init(app):
    from config import configs
    sys_log.info(msg=f'Start app with {configs.ENVIRONMENT} environment')
    if configs.ENVIRONMENT == 'production':
        server.docs_url = None
        server.redoc_url = None
        server.debug = False


async def start_event():
    await write_log(msg='系统启动')


async def shutdown_event():
    await write_log(msg='系统关闭')


def create_app():
    app = FastAPI(title="",
                  description="cnd平台用户模块接口文档",
                  version="1.0.0",
                  on_startup=[start_event],
                  on_shutdown=[shutdown_event]
                  )

    log_init()

    conf_init(app)

    # 初始化路由配置
    router_init(app)

    # 初始化中间件
    middleware_init(app)

    # 建表
    db_init(app)

    return app

# from typing import Optional
# from fastapi import FastAPI, Header, Body, Form
# from fastapi.responses import HTMLResponse, JSONResponse

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/user/{id}")
# def user(id):
#     return {
#         "id": id,
#     }


# @app.post("/login")
# def login(data=Body(None)):
#     return data


# @app.post("/form")
# def form(user_name=Form(default=""), password=Form(...)):
#     return {
#         "data": {
#             "user_name": user_name,
#             "password": password,
#         }
#     }


# @app.get("/jsonres")
# def jsonres():
#     return JSONResponse({"Hello": "World", "status": 200})


# @app.get("/htmlres")
# def htmlres():
#     return HTMLResponse("<h1>Hello World</h1>")


# @app.post("/items/save")
# def save_item():
#     return {
#         status: "success",
#         code: 200,
#     }
