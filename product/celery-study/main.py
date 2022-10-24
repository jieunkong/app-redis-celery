import uvicorn
from app import create_app
from config.app_config import AppConfig

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=AppConfig().APP_PORT)