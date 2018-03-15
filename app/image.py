import os
from PIL import Image, ImageOps
from uuid import uuid4

from .settings import CROPPED_IMAGE_DIR
from .utils import get_random_image

class PlaceholderImage:
  def __init__(self):
    self.image_file = get_random_image()
    self.cropped_image = None

  def crop(self, width: int, height: int):
    new_file = '{}.jpg'.format(uuid4())
    new_file_path = os.path.join(CROPPED_IMAGE_DIR, new_file)

    self.resizecrop(self.image_file, new_file_path, width, height)

    self.cropped_image = new_file_path

  def resizecrop(self, src, out, width, height):
    img = Image.open(src)
    img = ImageOps.fit(img, (width, height), Image.ANTIALIAS, 0, (0.5, 0.5))
    img.save(out)

  def get_file(self):
    return self.cropped_image if self.cropped_image else self.image_file

  def get_target_size(self, image, new_width, new_height) -> tuple:
    """Returns a tuple of (width,height)"""
    width, height = image.size
    if width > height:
      return (new_width, int((width / height) * new_height))
    return (new_height, int((height / width) * new_width))
