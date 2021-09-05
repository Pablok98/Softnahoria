import data_utils
from data_utils import to_excel
from board_obj import Board
from os import mkdir, getcwd, listdir
import os
from os.path import isdir, join
import json
from dotenv import load_dotenv
from requests_oauthlib import OAuth1, OAuth1Session
import fetcher
from board_obj import Board
# Cargamos archivo .env
load_dotenv()

# Cargamos parámetros
with open('../params.json', 'r') as file:
    params = json.load(file)

# Vemos si el directorio data existe
dir_path = join(getcwd(), params['outdir_name'])
if not isdir(dir_path):
    mkdir(dir_path)

# Autentificación
api_key = os.getenv('TR_KEY')
api_secret = os.getenv('TR_SECRET')
token = os.getenv('TR_OATH_TOKEN')
token_secret = os.getenv('TR_OATH_TOKEN_SECRET')
oauth = OAuth1(client_key=api_key, client_secret=api_secret,
                                resource_owner_key=token, resource_owner_secret=token_secret)

# Fetcheamos el estado actual de todos los grupos
for nombre, id_ in params["grupos"].items():
    target = join(dir_path, nombre, "raw")
    fetcher.fetch_board_meta(id_, target)

# Creamos los excel
entrega = params["n_entrega"]
for nombre in params["grupos"].keys():
    target = join(dir_path, nombre, "raw")
    excel_target = join(dir_path, nombre, "excel")
    for file in listdir(target):
        with open(join(target, file), 'r') as arch:
            tablero = Board(json.load(arch))
            data_utils.to_excel(tablero, excel_target, entrega, file.rstrip(".json"))
