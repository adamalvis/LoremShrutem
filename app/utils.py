import os
import random

from .settings import IMAGE_DIR


def get_random_image() -> str:
  """Selects a random image from image directory"""
  ignore_files = ['.DS_Store', 'cropped']
  images = [x for x in os.listdir(IMAGE_DIR) if x not in ignore_files]
  return '{}/{}'.format(IMAGE_DIR, random.choice(images))
