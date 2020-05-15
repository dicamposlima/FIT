import re

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = [
    {'login': 'aluno1', 'senha': 'azul'},
    {'login': 'aluno2', 'senha': 'vermelho'}
]
dados = {}

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html", mensagem="Entre no sistema")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", mensagem="Entre no sistema")

@app.route("/logout", methods=["POST"])
def logout():
    global dados
    dados = {}
    return render_template("login.html", mensagem="Entre no sistema")

@app.route("/form", methods=["PUT", "POST"])
def form_teste():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("login_ok.html", login=login)
    return render_template("login.html", mensagem="Login inválido.")


@app.route("/register", methods=["GET"])
def register():
    global dados
    dados = {'email': '', 'telefone': '', 'cep': '', 'nome': '', 'cpf': ''}
    return render_template("register.html", mensagem="CADASTRO", data=dados, valid=True)


@app.route("/save", methods=["POST"])
def save():
    global dados
    mensagem = ''
    email = request.form["email"]
    telefone = request.form["telefone"]
    cep = request.form["cep"]
    nome = request.form["nome"]
    cpf = request.form["cpf"]

    valido = True

    if not re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email):
        valido = False
        mensagem = 'EMAIL inválido<br>'

    if not re.search(r'^(?:[12][1-9]9[2-9]|[3-9][1-9][5-9])[0-9]{7}$', telefone):
        valido = False
        mensagem = f'{mensagem} TELEFONE inválido<br>'

    if not re.search(r'^[0-9]{8}$', cep):
        valido = False
        mensagem = f'{mensagem} CEP inválido. Formato: 00000000<br>'

    if len(nome) < 4:
        valido = False
        mensagem = f'{mensagem} NOME inválido. Somente letras. Quantidade mínima 4 caracteres.<br>'

    if not re.search(r'^[0-9]{11}$', cpf):
        valido = False
        mensagem = f'{mensagem} CPF inválido. Formato: 00000000000<br>'

    if not valido:
        dados = {'email': email, 'telefone': telefone, 'cep': cep, 'nome': nome, 'cpf': cpf}
        return render_template("register.html", mensagem=mensagem, data=dados, valid=valido)

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    json_data = response.json()
    if 'erro' in json_data:
        valido = False
        mensagem = f'{mensagem} CEP inválido<br>'
        return render_template("register.html", mensagem=mensagem, data=dados, valid=valido)

    dados = {'email': email, 'telefone': telefone, 'cep': {
        "cep": json_data['cep'],
        "logradouro": json_data['logradouro'],
        "bairro": json_data['bairro'],
        "localidade": json_data['localidade'],
        "uf": json_data['uf'],
    }, 'nome': nome, 'cpf': cpf}

    return render_template("show.html", mensagem='DADOS CADASTRADOS', data=dados, valid=valido)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
