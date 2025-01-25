from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .services.sprite_service import SpriteService
from .services.sound_service import SoundService
from .services.service_container import ServiceContainer
from .api.routes import sprite_routes, sound_routes
from .core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version=settings.VERSION,
)

sprite_service = SpriteService()
sound_service = SoundService()

@app.on_event("startup")
async def startup_event():
    #sprite_service.initialize_model()
    sound_service.initialize_model()

    ServiceContainer.initialize(
        sprite_service=sprite_service,
        sound_service=sound_service
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/temp_images", StaticFiles(directory="temp_images"), name="temp_images")
app.mount("/sounds", StaticFiles(directory="sounds"), name="sounds")

app.include_router(sprite_routes.router)
app.include_router(sound_routes.router)
