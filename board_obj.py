import json
import data_utils


class Board:
    def __init__(self, json_):
        self.meta_json = json_[0]
        self.json_ = json_[1:]
        self.name = self.meta_json['name']
        self.lists = []

        self.load_data()

    def load_data(self):
        for list_ in self.json_:
            id_ = list_['id']
            name = list_['name']
            cards_json = list_['cards']
            self.lists.append(List(id_, name, cards_json))

    def print_info(self):
        print("---------------------------------")
        print(f"        Tablero: {self.name}       ")
        print("---------------------------------")
        print()
        for lista in self.lists:
            lista.print_info()


class List:
    def __init__(self, id_, name, cards_json):
        self.id_ = id_
        self.name = name
        self.cards_json = cards_json
        self.cards = []

        self.load_data()

    def load_data(self):
        for card in self.cards_json:
            id_ = card['id']
            name = card['name']
            last_activity = card['dateLastActivity']
            desc = card['desc']
            id_members = card['idMembers']
            self.cards.append(Card(id_, name, last_activity, desc, id_members))

    def print_info(self):
        print(f" --- Lista: {self.name} ---")
        for card in self.cards:
            print(f"+ {card}")
        print()


class Card:
    def __init__(self, id_, name, last_activity, desc, id_members):
        self.id_ = id_
        self.name = name
        self.last_activity = last_activity
        self.description = desc
        self.membs_id = id_members

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with open('test_board.json', 'r') as arch:
        tablero = Board(json.load(arch))
    tablero.print_info()
    data_utils.to_excel(tablero)