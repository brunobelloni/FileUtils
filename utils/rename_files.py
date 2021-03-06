# USAGE: python rename_files.py 'dir'
# USAGE: python rename_files.py --dir 'DIR' --time True
# Rename Files order by ID

# Shell
# num=0; for i in *; do mv "$i" "$(printf '%04d' $num).${i#*.}"; ((num++)); done

import argparse
import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="dir")
parser.add_argument("--time", help="time", default=False, type=bool)
args = parser.parse_args()

if args.dir:
    pasta = args.dir
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = (arq for arq in caminhos if os.path.isfile(arq))

    for index, arquivo in enumerate(arquivos):
        name = "{:05}.png".format(index)
        if args.time:
            time = datetime.datetime.now().time().strftime("%Y-%m-%d-%I-%M-%S-%p")
            name = "{:05}-{}.png".format(index, time)
        new_name = os.path.join(os.path.dirname(arquivo), name)
        os.rename(arquivo, new_name)
