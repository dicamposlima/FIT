import sqlite3
from typing import List


class ItemNaoExisteException(Exception):
    pass


def heroi_tem_item(id_heroi: int) -> bool:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    item_do_heroi = cursor.execute("SELECT * FROM ItemDoHeroi WHERE idHeroi = (?)",
                                   [id_heroi]).fetchone()
    connection.close()
    return False if item_do_heroi is None else True


def heroi_quantos_itens(id_heroi: int) -> int:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    qtd = cursor.execute("SELECT count(*) FROM ItemDoHeroi WHERE idHeroi = (?)",
                         [id_heroi]).fetchone()
    connection.close()
    return qtd[0]


def consulta_itens_por_heroi(idHeroi: int) -> List:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    herois = cursor.execute("SELECT * FROM ItemDoHeroi WHERE idHeroi = (?)",
                            [idHeroi]).fetchall()
    connection.close()
    return [{
        'id': item_do_heroi[0],
        'idItem': item_do_heroi[1],
        'idHeroi': item_do_heroi[2],
    } for item_do_heroi in herois]


def dar_item_para_heroi(heroi: dict, item: dict) -> None:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    item_do_heroi = cursor.execute("SELECT * FROM ItemDoHeroi WHERE idItem = (?) AND idHeroi = (?)",
                                   [item['id'], heroi['id']]).fetchone()
    if item_do_heroi is None:
        cursor.execute("INSERT INTO ItemDoHeroi (idItem, idHeroi) VALUES (?, ?)",
                       [item['id'], heroi['id']])
        connection.commit()
    connection.close()
