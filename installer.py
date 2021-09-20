from os import mkdir, getcwd
from os.path import isdir, join, isfile
import json

import os

dir_path = join(getcwd(), "data")


def new_installation():
    if not isdir("data"):
        mkdir("data")
    json_ = {
              "outdir_name": "data",
              "n_entrega": 0,
              "grupos": {}
            }
    with open('params.json', 'w') as file:
        json.dump(json_, file)

