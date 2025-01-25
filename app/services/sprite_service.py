from fastapi import UploadFile, HTTPException
from typing import List
import torch
from diffusers import FluxPipeline 
import os, sys
import logging

from ..core.config import get_settings
from ..models.sprite_models import SpriteConfig, CreateSpriteResponse

settings = get_settings()

os.environ['HF_HOME'] = '/app/models'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

class SpriteService:
    def __init__(self):
        self.model_id = settings.MODEL_ID
        self.upload_dir = settings.UPLOAD_DIR
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        os.makedirs(self.upload_dir, exist_ok=True)
        self.pipe = None

    def initialize_model(self):
        self.pipe = FluxPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.bfloat16,
            cache_dir="/app/models/"
        )
        self.pipe = self.pipe.to(self.device)

        logger.info(f"Finished loading all models")

    async def create_sprite(self, input_config: SpriteConfig):
        try:
            image = self.pipe(
                prompt=input_config.prompt,
                height=1024, 
                width=1024,
                num_inference_steps=50,
                guidance_scale=3.5
            ).images[0]

            filename="example_1.png"
            image_path = os.path.join("temp_images", filename)

            image.save(image_path)
            
            return CreateSpriteResponse(
                message="Sprite Successfully Created",
                filename="http://localhost:8000/temp_images/example_1.png"
            )
        except Exception as e:
            logger.info(f"\n\n\n Failed with error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
