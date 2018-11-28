# USAGE: python main.py 'dir'

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="dir")
args = parser.parse_args()

if args.dir:
    pasta = args.dir
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    count = 0
    for arquivo in arquivos:
        name = str(count) + '.png'
        new_name = os.path.join(os.path.dirname(arquivo), name)
        os.rename(arquivo, new_name)
        count = count + 1
