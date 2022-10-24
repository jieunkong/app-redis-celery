from os import getenv
from pathlib import Path
from pydantic import BaseSettings
from common.utils.singleton import Singleton


class FinalMeta(type(BaseSettings), Singleton): ...

class AppConfig(BaseSettings, metaclass=FinalMeta):
    BASE_DIR: Path = Path.cwd()
    APP_NAME: str = getenv('APP_NAME', 'app')

    DEBUG_MODE: bool = getenv('DEBUG_MODE', True)
    APP_PORT: int = int(getenv('APP_PORT', 5000))

    class Config:
        pass

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__class__.__signature__)
