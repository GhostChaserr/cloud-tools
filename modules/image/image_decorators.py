import time
from fastapi import Request
from functools import wraps
from .image_dto import SendImageDto
from helpers.global_helpers import global_helpers

def extract_images(func):
  @wraps(func)
  async def wrapper(request: Request, sendImageDto: SendImageDto, *args, **kwargs):
    np_imgs = []
    
    for base64 in sendImageDto.images:
      np_img = global_helpers.decode_base64(base64=base64)
      np_imgs.append(np_img)

    request.state.np_imgs = np_imgs 
    return await func(request, sendImageDto, *args, **kwargs)
  return wrapper