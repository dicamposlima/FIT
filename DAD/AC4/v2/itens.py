import sqlite3
from typing import Dict


class ItemNaoExisteException(Exception):
    pass


def consultar_item(id_item: int) -> Dict:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    item = cursor.execute("SELECT * FROM Item WHERE id = (?)",
                          [id_item]).fetchone()
    if item is None:
        raise ItemNaoExisteException
    connection.close()
    item = {
        'id': item[0],
        'nome': item[1],
        'tipo': item[2],
        'fisico': item[3],
        'magia': item[4],
        'agilidade': item[5],
        'emUso': item[6]
    }
    return item


def nome_para_id_item(item_nome: str) -> int:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    item = cursor.execute("SELECT id FROM Item WHERE nome = (?)",
                          [item_nome]).fetchone()
    if item is None:
        raise ItemNaoExisteException
    connection.close()
    return item[0]


def criar_item(tipo: str, nome: str, fisico: int, agilidade: int, magia: int) -> None:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    item = cursor.execute("SELECT * FROM Item WHERE nome = (?)",
                          [nome]).fetchone()
    if item is None:
        cursor.execute("INSERT INTO Item (tipo, nome, fisico, agilidade, magia, emUso) VALUES (?, ?, ?, ?, ?, ?)",
                       [tipo, nome, fisico, agilidade, magia, 0])
        connection.commit()
    connection.close()


def colocar_item_em_uso(item: dict) -> None:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Item SET emUso=? WHERE id = ?",
                   [1, item['id']])
    connection.commit()
    connection.close()
