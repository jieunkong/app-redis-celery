import uvicorn
from app import create_app
from app.routers import api_router
from config.app_config import AppConfig

app = create_app()
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=AppConfig().APP_PORT)