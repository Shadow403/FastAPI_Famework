import uvicorn
from app.app import app
from config.config import WebAPI

if __name__ == "__main__":
    uvicorn.run(app, host=WebAPI.HOST, port=WebAPI.PORT)
