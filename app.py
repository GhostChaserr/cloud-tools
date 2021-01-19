from typing import Optional
from fastapi import FastAPI
from db.conn import db

# Load Tables.
from modules.shared.shared_models import Activity


app = FastAPI()

@app.on_event("startup")
async def handle_request():

    # Connect to db
    db.connect()

    # Register tables.
    db.create_tables([Activity])


@app.on_event("shutdown")
async def handle_request():
    db.close()

from modules.image import image_routes
from modules.app import app_routes
from modules.shared import shared_routes

