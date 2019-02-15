# USAGE: python rename_files.py 'dir'
# Rename Files order by ID

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="dir")
args = parser.parse_args()

if args.dir:
    pasta = args.dir
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

    for arquivo in arquivos:
        name = str(arquivos.index(arquivo)) + '.png'
        new_name = os.path.join(os.path.dirname(arquivo), name)
        os.rename(arquivo, new_name)
