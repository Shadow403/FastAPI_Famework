from config.config import WebAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from utils import *

app = FastAPI()

@app.get("/")
async def read_root():
    return ret_200(data={
        "server_time": await func_nowtime(info=True),
        "server_ntsp": await func_nowtime(timestamp=True)
    })

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=404,
        content=WebAPI._c_404,
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=WebAPI._c_500,
    )
