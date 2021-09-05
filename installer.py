from os import mkdir, getcwd
from os.path import isdir, join, isfile
import json

dir_path = join(getcwd(), "data")


def new_installation():
    if not isdir(dir_path):
        mkdir(dir_path)
    json_ = {
              "outdir_name": "data",
              "n_entrega": 0,
              "grupos": {}
            }
    with open('params.json', 'w') as file:
        json.dump(json_, file)