import sqlite3
from typing import List


class ItemNaoExisteException(Exception):
    pass


def consulta_itens_por_heroi(idHeroi: int) -> List:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()

    sql = "SELECT * FROM ItemDoHeroi WHERE idHeroi = (?)"
    cursor.execute(sql, [idHeroi])

    herois = cursor.fetchall()
    # if len(herois) <= 0:
    # raise ItemNaoExisteException

    itens_dos_herois = []
    for item_do_heroi in herois:
        itens_dos_herois.append({
            'id': item_do_heroi[0],
            'idItem': item_do_heroi[1],
            'idHeroi': item_do_heroi[2],
        })

    connection.close()
    return itens_dos_herois


def dar_item_para_heroi(heroi: dict, item: dict) -> None:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM ItemDoHeroi WHERE idItem = (?) AND idHeroi = (?)"
    cursor.execute(sql, [item['id'], heroi['id']])

    item_do_heroi = cursor.fetchone()
    if item_do_heroi is None:
        sql = "INSERT INTO ItemDoHeroi (idItem, idHeroi) VALUES (?, ?)"
        cursor.execute(sql, [item['id'], heroi['id']])
        connection.commit()
    connection.close()
