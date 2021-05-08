from app import app
from fastapi import Request
from functools import wraps
from fastapi import Depends

from modules.shared.shared_decorators import activity

from helpers.global_helpers import global_helpers
from .image_decorators import extract_images

from .image_dto import (
    SendImageDto,
    ResizeImageDto,
    CompressImageDto,
    TrademarkImageDto,
    ScaleImageDto,
)
from .image_service import image_service


@app.get('/api/image')
async def handle_request(request: Request):
    return {"Hello": "IMG SERVICE"}


@app.post('/api/image/convert-blackwhite', tags=["images"])
@activity("CONVER_IMG_BLACK_TO_WHITE")
@extract_images
async def handle_request(request: Request, sendImageDto: SendImageDto):
    response = {"images": []}

    for img_source in request.state.np_imgs:
        result_nparr = image_service.convert_blackwhite(img_source=img_source,
                                                        tresh_intensity=sendImageDto.tresh_intensity)
        result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
        response['images'].append(result_img)

    return response


@app.post('/api/image/scale', tags=["images"])
@activity("SCALE_IMAGE")
@extract_images
async def handle_request(request: Request, sendImageDto: SendImageDto):
    response = {"images": []}

    for img_source in request.state.np_imgs:
        result_nparr = image_service.scale_img(img_source=img_source, scale_percentage=sendImageDto.scale_percentage)
        result_image = global_helpers.nparray_tobase64(np_arr=result_nparr)

        response['images'].append(result_image)
    return response


@app.post('/api/image/convert-grayscale', tags=["users"])
async def handle_request(sendImageDto: SendImageDto):
    response = {"images": []}

    for base64 in sendImageDto.images:
        img_source = global_helpers.decode_base64(base64=base64)
        result_nparr = image_service.convert_grayscale(img_source=img_source)

        result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
        response['images'].append(result_img)

    return response


@app.post('/api/image/crop_img', tags=["users"])
async def handle_request(sendImageDto: SendImageDto):
    response = {"images": []}

    for base64 in sendImageDto.images:
        img_source = global_helpers.decode_base64(base64=base64)
        result_nparr = image_service.crop_img(img_source=img_source, cordinates=sendImageDto.cordinates)
        result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)
        response['images'].append(result_img)

    return response


@app.post('/api/image/resize_img', tags=["users"])
async def handle_request(resizeImageDto: ResizeImageDto):
    response = {"images": []}

    for base64 in resizeImageDto.images:
        img_source = global_helpers.decode_base64(base64=base64)

        operation_result = image_service.resize_img(
            img_source=img_source,
            template=resizeImageDto.template,
            dimensions=resizeImageDto.dimensions
        )

        result_img = global_helpers.nparray_tobase64(np_arr=operation_result)
        response['images'].append(result_img)

    return response


@app.post('/api/image/trademark_img', tags=["users"])
async def handle_request(trademarkImageDto: TrademarkImageDto):
    response = {"images": [], "errors": []}
    trademark_source = global_helpers.decode_base64(base64=trademarkImageDto.trademark)

    for base64 in trademarkImageDto.images:
        target_source = global_helpers.decode_base64(base64=base64)

        operation_result = image_service.trademark_img(
            trademark_source=trademark_source,
            dimensions=trademarkImageDto.dimensions,
            target_source=target_source,
            x_offset=trademarkImageDto.x_offset,
            y_offset=trademarkImageDto.y_offset
        )

        if operation_result['data'] is None:
            response['images'] = []
            response['errors'].append(operation_result['error'])
            break

        result_img = global_helpers.nparray_tobase64(np_arr=operation_result['data'])
        response['images'].append(result_img)

    return response


@app.post('/api/image/compress_img', tags=["users"])
async def handle_request(compressImageDto: CompressImageDto):
    response = {"images": []}

    for base64 in compressImageDto.images:
        img_source = global_helpers.decode_base64(base64=base64)
        result_nparr = image_service.compress_img(img_source=img_source, quality=compressImageDto.quality)
        result_img = global_helpers.nparray_tobase64(np_arr=result_nparr)

        response['images'].append(result_img)

    return response
