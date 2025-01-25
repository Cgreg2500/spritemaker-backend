from fastapi import HTTPException
import os, sys
import logging
import torch
import torchaudio
from tangoflux import TangoFluxInference
from scipy.io import wavfile

from ..core.config import get_settings
from ..models.sound_models import CreateSoundRequest, CreateSoundResponse

settings = get_settings()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

class SoundService:
    def __init__(self):
        self.model_id = settings.SOUND_MODEL_ID
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = None

    def initialize_model(self):
        self.pipe = TangoFluxInference(self.model_id)

        logger.info("Finished loading all models")

    async def create_sound(self, input_request: CreateSoundRequest):
        try:
            audio_data = self.pipe.generate(
                input_request.prompt,
                steps=50,
                duration=10
            )

            wavfile.write(
                os.path.join("sounds", "example_1.wav"),
                44100,
                audio_data
            )

            return CreateSoundResponse(
                message="Sound Successfully Created",
                filename="http://localhost:8000/sounds/example_1.wav"
            )
        except Exception as e:
            logger.info(f"\n\n\n Failed with error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
