from flask import Flask, request, jsonify
from to_dict import *
from validacao import *

treinadores = {}

class PokemonJaExisteException:
    pass

class Treinador:
    def __init__(self, nome):
        self.__nome = nome
        self.__pokemons = {}

    @property
    def nome(self):
        return self.__nome

    @property
    def pokemons(self):
        return self.__pokemons

    def adicionar_pokemon(self, apelido, tipo, experiencia):
        if apelido in self.__pokemons: raise PokemonJaExisteException()
        self.__pokemons[apelido] = Pokemon(apelido, tipo, experiencia)

class Pokemon:
    def __init__(self, apelido, tipo, experiencia):
        self.__apelido = apelido
        self.__tipo = tipo
        self.__experiencia = experiencia

    @property
    def apelido(self):
        return self.__apelido

    @property
    def tipo(self):
        return self.__tipo

    @property
    def experiencia(self):
        return self.__experiencia

    def ganhar_experiencia(self, ganho):
        self.__experiencia += ganho

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Pikachu, eu escolho você!"

@app.route("/reset", methods = ["POST"])
def reset():
    treinadores.clear()
    return "Equipe Rocket decolando na velocidade da luz!"

@app.route("/treinador")
def listar_treinadores():
    return jsonify(to_dict(treinadores))

@app.route("/treinador/<nome>")
def detalhar_treinador(nome):
    if nome not in treinadores: return "", 404
    return jsonify(to_dict(treinadores[nome]))

@app.route("/treinador/<nome>/<apelido>")
def detalhar_pokemon(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    return jsonify(to_dict(pokemons[apelido]))

@app.route("/treinador/<nome>", methods = ["PUT"])
def cadastrar_treinador(nome):
    if nome in treinadores: return jsonify(to_dict(treinadores[nome])), 303
    t = Treinador(nome)
    treinadores[nome] = t
    return jsonify(to_dict(t)), 202

@app.route("/treinador/<nome>", methods = ["DELETE"])
def excluir_treinador(nome):
    if nome not in treinadores: return "", 404
    del treinadores[nome]
    return "", 204

@app.route("/treinador/<nome>/<apelido>", methods = ["PUT"])
def cadastrar_pokemon(nome, apelido):
    if nome not in treinadores: return "", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido in pokemons: return "", 409
    dados = request.get_json()
    validar_campos(dados, {'tipo': str_nao_vazio, 'experiencia': natural})
    pokemon = treinador.adicionar_pokemon(apelido, dados['tipo'], dados['experiencia'])
    return jsonify(to_dict(pokemon)), 202

@app.route("/treinador/<nome>/<apelido>/exp", methods = ["POST"])
def adicionar_experiencia(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    pokemon = pokemons[apelido]
    dados = request.get_json()
    validar_campos(dados, {'experiencia': natural})
    pokemon.ganhar_experiencia(dados['experiencia'])
    return "", 204

@app.route("/treinador/<nome>/<apelido>", methods = ["DELETE"])
def excluir_pokemon(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    del pokemons[apelido]
    return "", 204

if __name__ == "__main__":
    app.run(port = 9000)