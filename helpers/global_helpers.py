import re
import base64
from PIL import Image
import cv2
from io import StringIO
from io import BytesIO
import numpy as np
from logging import exception

class GlobalHelpers:
  def __init__(self):
    pass

  def nparray_tobase64(self, np_arr=None):

    if np_arr is None:
      raise Exception('Np array failed!')

    pil_img = Image.fromarray(np_arr)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    image = base64.b64encode(buff.getvalue()).decode("utf-8")

    return image

  def extract_base64(self, base64=None):
    try:
      image = re.sub('^data:image/.+;base64,', '', base64)
      return image
    except exception as _ex:
      return image

    return image

  def base64_to_cv2(self, encoded_base64=None):

    if encoded_base64 is None:
      raise Exception('Base 64 image is missing!')

    nparr = np.fromstring(base64.b64decode(encoded_base64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return img

  def decode_base64(self, base64=None):

    if base64 is None:
      return
    
    encoded_base64 = self.extract_base64(base64=base64)
    img = self.base64_to_cv2(encoded_base64=encoded_base64)

    return img

global_helpers = GlobalHelpers()