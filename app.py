from typing import Optional
from fastapi import FastAPI

app = FastAPI()

from modules.image import image_routes
from modules.app import app_routes


