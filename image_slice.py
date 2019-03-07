# USAGE: python image_slice.py --image image.png --x 10 --y 5

import argparse
import cv2
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image to be processed", required=True)
parser.add_argument("--x", type=int, required=False)
parser.add_argument("--y",  type=int, required=False)
args = parser.parse_args()

image = cv2.imread(args.image)


def slice(image, slice_x=2, slice_y=2):
    height, width = image.shape[:2]
    half_x, half_y = int(height/slice_x), int(width/slice_y)
    image_list = [image[x:x+half_x, y:y+half_y]
                  for x in range(0, height, half_x) for y in range(0, width, half_y)]

    return image_list


images = slice(image)

for index, image in enumerate(images):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_DIR = os.path.join(BASE_DIR, 'imgs')
    os.makedirs(IMAGE_DIR, exist_ok=True)

    name = "{}_slice_{}.png".format(time.time(), index)
    IMAGE_DIR = os.path.join(IMAGE_DIR, name)

    cv2.imwrite(IMAGE_DIR, image)
