from app import app
from .shared_models import Activity
import json
import math

@app.get("/api/activities")
async def read_root(page: int = 1, limit: int = 100):

    total = Activity.select().count()
    pages = math.ceil(total / limit)

    activities = list(Activity.select().paginate(page, limit).dicts())

    response = {
      "total": total,
      "page": page,
      "limit": limit,
      "pages": pages,
      "records": activities
    }

    return response
