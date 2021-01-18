from typing import Optional, List
from pydantic import BaseModel

class SendImageDto(BaseModel):
    images: List[str]
    tresh_intensity: Optional[List[int]]
    cordinates: Optional[List[int]]


class ResizeImageDto(BaseModel):
    template: Optional[str]
    images: List[str]
    dimensions: List[int]


class TrademarkImageDto(BaseModel):
    x_offset: int
    y_offset: int
    dimensions: List[int]
    trademark: str
    images: List[str]

class CompressImageDto(BaseModel):
    images: List[str]
    quality: int