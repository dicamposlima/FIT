import sqlite3
from typing import Dict


class HeroiNaoExisteException(Exception):
    pass


def heroi_existe(id_heroi: int) -> bool:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    heroi = cursor.execute("SELECT * FROM Heroi WHERE id = (?)",
                           [id_heroi]).fetchone()
    connection.close()
    return False if heroi is None else True


def consultar_heroi(id_heroi: int) -> Dict:
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    heroi = cursor.execute("SELECT * FROM Heroi WHERE id = (?)",
                           [id_heroi]).fetchone()
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
    heroi = cursor.execute("SELECT * FROM Heroi WHERE nome = (?)",
                           [nome_heroi]).fetchone()
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
    heroi = cursor.execute("SELECT * FROM Heroi WHERE nome = (?)",
                           [nome]).fetchone()
    if heroi is None:
        cursor.execute("INSERT INTO Heroi (nome, agilidade, fisico, magia) VALUES (?, ?, ?, ?)",
                       [nome, agilidade, fisico, magia])
        connection.commit()
    connection.close()
