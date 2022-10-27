from fastapi import FastAPI
from config.app_config import AppConfig



def create_app():
    app = FastAPI()

    app_pwd = AppConfig().BASE_DIR
    app_name = AppConfig().APP_NAME

    
    return app