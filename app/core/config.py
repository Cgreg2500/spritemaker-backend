import torch
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Sprite Sheet Creator"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    UPLOAD_DIR: str = "temp_uploads"
    MAX_UPLOAD_SIZE: int = 10_485_760 # 10MB
    ALLOWED_EXTENSIONS: set = {"png", "jpg", "jpeg", "gif"}
    MODEL_ID: str = "black-forest-labs/FLUX.1-dev"
    SOUND_MODEL_ID: str = "declare-lab/TangoFlux"

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
