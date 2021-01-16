from typing import Optional, List
from pydantic import BaseModel

class SendImageDto(BaseModel):
    images: List[str]
    tresh_intensity: Optional[List[int]]
    cordinates: Optional[List[int]]


class ResizeImageDto(BaseModel):
    images: List[str]
    dimensions: List[int]


class CompressImageDto(BaseModel):
    images: List[str]
    quality: int