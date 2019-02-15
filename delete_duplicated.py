# USAGE: python delete_duplicated.py 'dir'
# Delete Duplicated Images

import os
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="dir")
args = parser.parse_args()
list_to_remove = set()
image_list = []
index = 0

def is_duplicated(image, aux):
    if image.shape == aux.shape:
        difference = cv2.subtract(image, aux)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
    return False

if args.dir:
    pasta = args.dir
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    image_list = [cv2.imread(image) for image in arquivos]


    for image, arquivos in zip(image_list, arquivos):
        for aux in image_list[index+1:]:
            if is_duplicated(image, aux):
                list_to_remove.add(arquivos)
        index = index + 1


print(len(list_to_remove), 'files to remove!')
for remove in list_to_remove:
    os.remove(remove)
    print(os.path.basename(remove), 'deleted!')
