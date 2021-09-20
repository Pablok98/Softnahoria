import os
import argparse
import json
from dotenv import load_dotenv
from os.path import join
from os import getcwd, listdir

import installer



# -------------------------------------------
# //           Command parser              //
# -------------------------------------------


def main():
    # Cambio temporal de directorio por el bugfix de comandos en consola
    os.chdir(join(getcwd(), 'softnahoria'))
    parser = argparse.ArgumentParser(description="Ayudante helper")
    parser.add_argument("command", help="Comando a correr")
    args = parser.parse_args()

    if args.command == "install":
        installer.new_installation()
        exit()
    print(getcwd())
    import data_utils
    import fetcher
    from board_obj import Board
    import oauth_helper
    # Cargamos archivo .env
    load_dotenv()
    # Cargamos parámetros
    json_path = join(getcwd(), 'params.json')
    with open(json_path, 'r') as file:
        params = json.load(file)
    dir_path = join(getcwd(), params['outdir_name'])

    if args.command == "oath":
        oauth_helper.token_creator()

    if args.command == "newgroup":
        name = input("Nombre del grupo:")
        link = input("Link a su tablero")
        data_utils.make_group(name, link)

    if args.command == "update":
        for nombre, id_ in params["grupos"].items():
            target = join(dir_path, nombre, "raw")
            fetcher.fetch_board_meta(id_, target)

    if args.command == "excel":
        entrega = params["n_entrega"]
        for nombre in params["grupos"].keys():
            target = join(dir_path, nombre, "raw")
            excel_target = join(dir_path, nombre, "excel")
            for file in listdir(target):
                with open(join(target, file), 'r') as arch:
                    tablero = Board(json.load(arch))
                    data_utils.to_excel(tablero, excel_target, entrega, file.rstrip(".json"))