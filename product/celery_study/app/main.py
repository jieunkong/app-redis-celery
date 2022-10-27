import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(sys.path)
from app import create_app
import uvicorn
from app.routers import api_router


from config.app_config import AppConfig

app = create_app()
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=AppConfig().APP_PORT)