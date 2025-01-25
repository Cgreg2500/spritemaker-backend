from fastapi import APIRouter

from ...models.sound_models import CreateSoundRequest, CreateSoundResponse
from ...services.service_container import ServiceContainer

router = APIRouter(prefix="/api/sound")

@router.post("/create-sound/")
async def create_sound(
    request: CreateSoundRequest
) -> CreateSoundResponse:
    return await ServiceContainer.get_sound_service().create_sound(request)
