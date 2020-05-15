import sqlite3
from typing import Dict


class HeroiNaoExisteException(Exception):
    pass


def consultar_heroi(id_heroi: int) -> Dict:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()

    sql = "SELECT * FROM Heroi WHERE id = (?)"
    cursor.execute(sql, [id_heroi])

    heroi = cursor.fetchone()
    if heroi is None:
        raise HeroiNaoExisteException

    connection.close()
    heroi = {
        'id': heroi[0],
        'nome': heroi[1],
        'fisico': heroi[2],
        'magia': heroi[3],
        'agilidade': heroi[4]
    }
    return heroi


def consultar_heroi_por_nome(nome_heroi: str) -> Dict:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()

    sql = "SELECT * FROM Heroi WHERE nome = (?)"
    cursor.execute(sql, [nome_heroi])

    heroi = cursor.fetchone()
    if heroi is None:
        raise HeroiNaoExisteException

    connection.close()
    heroi = {
        'id': heroi[0],
        'nome': heroi[1],
        'fisico': heroi[2],
        'magia': heroi[3],
        'agilidade': heroi[4]
    }
    return heroi


def criar_heroi(nome, agilidade, fisico, magia):
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Heroi WHERE nome = (?)"
    cursor.execute(sql, [nome])

    heroi = cursor.fetchone()
    if heroi is None:
        sql = "INSERT INTO Heroi (nome, agilidade, fisico, magia) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, [nome, agilidade, fisico, magia])
        connection.commit()
    connection.close()
