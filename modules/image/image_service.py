import cv2
from PIL import Image
from io import BytesIO
from helpers.global_helpers import global_helpers
from .image_helper import generate_random_treshhold
from .image_utils import templates

import numpy as np

class ImageService:
  def __init__(self):
    pass

  def trademark_img(self, trademark_source = None, target_source = None, x_offset = 0, y_offset = 0, dimensions = []):
    try:
      
      trademark_img = None
      if len(dimensions) > 0:
        trademark_resized_img = cv2.resize(trademark_source, dsize=(dimensions[0], dimensions[1]))
        trademark_img = cv2.cvtColor(trademark_resized_img, cv2.COLOR_BGRA2RGB)

      else:
        trademark_img = cv2.cvtColor(trademark_source, cv2.COLOR_BGRA2RGB)

      target_img = cv2.cvtColor(target_source, cv2.COLOR_BGR2RGB)
      target_img[y_offset:y_offset + trademark_img.shape[0], x_offset:x_offset + trademark_img.shape[1]] = trademark_img

      return { 'data': target_img, 'error': None }

    except Exception as ex:
      return { 'data': None, 'error': str(ex) }

  def crop_img(self, img_source=None, cordinates=[0, 0, 10, 10]):

    if img_source is None or len(cordinates) != 4:
      raise Exception('Invalid values')

    roi = img_source[cordinates[0]:cordinates[2], cordinates[1]:cordinates[3]]
    return roi
  

  def convert_grayscale(self, img_source=None):
    if img_source is None:
      raise Exception('Provide image source')

    gray_img = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    return gray_img

  def convert_blackwhite(self, img_source=None, tresh_intensity=[120, 255]):
    if img_source is None:
      raise Exception('Provide image source')

    # TODO. More on treshholding.
    # https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
    gray_img = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    (thresh, bw_img) = cv2.threshold(gray_img,  tresh_intensity[0], tresh_intensity[1], cv2.THRESH_BINARY)
    return bw_img

  
  def resize_img(self, img_source=None, dimensions=None, template=None):

    # First we check if template was provided!
    if template is not None:
      dimensions = templates[template]
      resized = cv2.resize(img_source, (dimensions[0], dimensions[1])) 
      return resized

    # Without template dimensions are needed
    if dimensions is None or len(dimensions) < 1:
      raise Exception('Bad request invalid dimensions!')

    resized = cv2.resize(img_source, (dimensions[0], dimensions[1])) 
    return resized

  def compress_img(self, img_source=None, quality=90):
    mem = BytesIO()

    # Save in memory
    im = Image.fromarray(np.uint8(img_source))
    im.save(mem, format="png", optimize=True, quality=quality)

    image = Image.open(mem)
    img_array = np.array(image)
    return img_array
  
image_service = ImageService()