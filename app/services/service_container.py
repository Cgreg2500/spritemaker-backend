from typing import Optional
from .sprite_service import SpriteService
from .sound_service import SoundService

class ServiceContainer:
    _instance = None
    sprite_service: Optional[SpriteService] = None
    sound_service: Optional[SoundService] = None

    @classmethod
    def initialize(cls,
        sprite_service: SpriteService,
        sound_service: SoundService
    ):
        if not cls._instance:
            cls._instance = cls()
        cls._instance.sprite_service = sprite_service
        cls._instance.sound_service = sound_service

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            raise RuntimeError("ServiceContainer is not initialized")
        return cls._instance

    @classmethod
    def get_sprite_service(cls) -> SpriteService:
        instance = cls.get_instance()
        if not instance.sprite_service:
            raise RuntimeError("SpriteService not initialized")
        return instance.sprite_service

    @classmethod
    def get_sound_service(cls) -> SoundService:
        instance = cls.get_instance()
        if not instance.sound_service:
            raise RuntimeError("SoundService not initialized")
        return instance.sound_service
