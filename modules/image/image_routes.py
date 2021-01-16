from app import app
from fastapi import Request
from .image_dto import SendImageDto, ResizeImageDto, CompressImageDto
from .image_service import image_service
from fastapi import Depends
from helpers.global_helpers import global_helpers

@app.get('/api/image')
async def handle_request():
    return {"Hello": "IMG SERVICE"}

@app.post('/api/image/convert-blackwhite')
async def handle_request(sendImageDto: SendImageDto):
  response = { "images": [] }

  for base64 in sendImageDto.images:

    img_source = global_helpers.decode_base64(base64=base64)
    result_nparr = image_service.convert_blackwhite(img_source=img_source, tresh_intensity=sendImageDto.tresh_intensity)

    result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
    response['images'].append(result_img)
    
  return response


@app.post('/api/image/convert-grayscale')
async def handle_request(sendImageDto: SendImageDto):
  response = { "images": [] }

  for base64 in sendImageDto.images:

    img_source = global_helpers.decode_base64(base64=base64)
    result_nparr = image_service.convert_grayscale(img_source=img_source)

    result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
    response['images'].append(result_img)
    
  return response

@app.post('/api/image/crop_img')
async def handle_request(sendImageDto: SendImageDto):
  response = { "images": [] }

  for base64 in sendImageDto.images:
    img_source = global_helpers.decode_base64(base64=base64)
    result_nparr = image_service.crop_img(img_source=img_source, cordinates=sendImageDto.cordinates)
    result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
    response['images'].append(result_img)

  return response

@app.post('/api/image/resize_img')
async def handle_request(resizeImageDto: ResizeImageDto):

  response = { "images": [] }
  
  for base64 in resizeImageDto.images:
    img_source = global_helpers.decode_base64(base64=base64)
    result_nparr = image_service.resize_img(img_source=img_source, dimensions=resizeImageDto.dimensions)
    result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
    response['images'].append(result_img)

  return response

@app.post('/api/image/compress_img')
async def handle_request(compressImageDto: CompressImageDto):

  response = { "images": [] }
  
  for base64 in compressImageDto.images:
    img_source = global_helpers.decode_base64(base64=base64)
    result_nparr = image_service.compress_img(img_source=img_source, quality=compressImageDto.quality)
    result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)

    response['images'].append(result_img)

  return response