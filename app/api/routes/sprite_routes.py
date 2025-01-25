from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
from typing import List
from ...models.sprite_models import SpriteConfig, SpriteUploadResponse
from ...services.sprite_service import SpriteService
from ...services.service_container import ServiceContainer
from ...core.config import get_settings

router = APIRouter(prefix="/api/v1")


@router.post("/create-sprite/")
async def create_sprite(
    config: SpriteConfig,
):
    return await ServiceContainer.get_sprite_service().create_sprite(config)
