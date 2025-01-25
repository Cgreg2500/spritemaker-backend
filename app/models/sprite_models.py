from pydantic import BaseModel, Field
from typing import List

class SpriteConfig(BaseModel):
    prompt: str

class CreateSpriteResponse(BaseModel):
    message: str
    filename: str

class SpriteSheetConfig(BaseModel):
    sprite_width: int = Field(..., gt=0)
    sprite_height: int = Field(..., gt=0)
    columns: int = Field(..., gt=0)
    padding: int = Field(0, gt=0)
    background_color: str = "transparent"

class SpriteUploadResponse(BaseModel):
    message: str
    filenames: List[str]

