class WebAPI:
    HOST = "0.0.0.0"
    PORT = 5001
    PREFIX: str = "/api"
    _c_404: dict = {"code": 404, "message": "notfound", "data": {}}
    _c_500: dict = {"code": 500, "message": "internal server error", "data": {}}
