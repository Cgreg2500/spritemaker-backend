from pydantic import BaseModel

class CreateSoundRequest(BaseModel):
    prompt: str

class CreateSoundResponse(BaseModel):
    message: str
    filename: str
