import datetime
from os import mkdir, getcwd
from os.path import isdir, join, isfile

import pandas as pd
import json

from fetcher import fetch_board_id

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


def make_group(name, link):
    id_ = fetch_board_id(link)
    tg_path = join(dir_path, name)
    if isdir(tg_path):
        print("Ese grupo ya existe!")
        return
    mkdir(tg_path)
    mkdir(join(tg_path, "raw"))
    mkdir(join(tg_path, "excel"))
    with open("params.json", "r") as file:
        params = json.load(file)
    params["grupos"][name] = id_
    with open("params.json", "w") as file:
        json.dump(params, file, indent=2)
    with open(join(tg_path, "meta.json"), "w") as file:
        json_ = {"id": id_}
        json.dump(json_, file, indent=2)


def to_excel(board, target_dir, entrega, hoja):
    if not isdir(target_dir):
        print("Error encontrando el objetivo de excel")
        return
    file_name = "-".join(board.name.split(" "))
    file_name += f"[E{entrega}]"
    excel_path = join(target_dir, f"{file_name}.xlsx")

    output_df = pd.DataFrame()
    for lista in board.lists:
        cards = []
        for card in lista.cards:
            cards.append(card.name)
        output_df = pd.concat([output_df, pd.DataFrame({lista.name: cards})], axis=1)
    sheet_name = hoja

    if not isfile(excel_path):
        empty_df = pd.DataFrame()
        empty_df.to_excel(excel_path, sheet_name=sheet_name, index=False)

    current_df = pd.read_excel(excel_path, sheet_name=None)
    current_df[sheet_name] = output_df

    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')

    for sheet, frame in current_df.items():
        frame.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()


if __name__ == "__main__":
    make_group("420", "https://trello.com/b/M4QRcp3l/2021-2")