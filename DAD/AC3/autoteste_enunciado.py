#!bin/python
from flask import Flask, jsonify, request
import copy

app = Flask(__name__)

questoes_iniciais = [
    {
        'id': 1,
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro'],
        'corretas': ['Remote procedure call']
    },
    {
        'id': 2,
        'pergunta': 'Quanto vale 2**6?',
        'erradas': [12, 36, 26, 32],
        'corretas': [64]
    }
]

respostas_iniciais = {
    'marcio': {1: 'Random Person Changer'},
    'maria': {1: 'Remote Procedure Call', 2: 64},
}

respostas = {}
questoes = []


def reseta():
    global respostas
    global questoes
    respostas = copy.deepcopy(respostas_iniciais)
    questoes = copy.deepcopy(questoes_iniciais)


reseta()  # quando eu rodo isso eu crio as variaveis respostas e questoes


# se sao as variaveis que você deve manipular


@app.route('/autoteste/reseta', methods=['POST'])
def reseta_request():
    reseta()
    return {'status': 'resetado'}


@app.route('/')
def index():
    return "Testes automáticos!"


'''
REPARE:

Você deve alterar os objetos respostas e questoes

NAO ALTERE NUNCA os objetos respostas_iniciais e questoes_iniciais
'''


def get_questao(id_questao: int):
    for questao in questoes:
        if questao["id"] == id_questao:
            return questao
    return None


'''
Ao acessar a URL /autoteste/questoes o usuario deve receber
uma lista completa de todas as questoes
'''


@app.route('/autoteste/questoes', methods=['GET'])
def get_questoes():
    return jsonify(questoes)


@app.route('/autoteste/respostas', methods=['GET'])
def get_respostas():
    return jsonify(respostas)


'''
Podemos acessar uma questao especifica na URL
/autoteste/questao/<int:q_id>

Se a questao existir, retorne a questao

Se nao existir, retorne um texto de erro e o codigo 404
'''


@app.route('/autoteste/questao/<int:q_id>', methods=['GET'])
def get_questao_by_id(q_id):
    questao = get_questao(q_id)
    if questao:
        return jsonify(questao), 200

    return {"erro": "Questao nao encontrada"}, 404


'''
Ao usarmos o verbo POST na url autoteste/questao

queremos criar uma nova questao.

no corpo da mensagem, enviamos o texto da questao (na chave pergunta),
uma lista de alternativas incorretas (na chave erradas) e uma lista
de alternativas corretas (na chave corretas).

Por exemplo:
    {
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    }

voce deve armazenar essa nova questao e retornar 
uma representacao JSON dela, com o codigo 201 (created)

Se um dos 3 campos estiver faltando, voce deve retornar um 
texto de erro, e o codigo 400
'''


@app.route('/autoteste/questao', methods=['POST'])
def add_questao():
    nova_questao = request.json

    if not nova_questao.get("pergunta"):
        return {"erro": 'Campo [pergunta] nao enviado'}, 400
    if not nova_questao.get("erradas"):
        return {"erro": 'Campo [erradas] nao enviado'}, 400
    if not nova_questao.get("corretas"):
        return {"erro": 'Campo [corretas] nao enviado'}, 400

    nova_questao["id"] = get_next_id()

    questoes.append(nova_questao)

    return jsonify(nova_questao), 201


'''
Agora melhore sua funçao, fazendo com que, ao ser acrescentada uma
questão, ela automaticamente ganhe a próxima id disponível

(isso não necessariamente vai ser usado no proximo teste, mas vai
ser importante eventualmente)
'''


def get_next_id() -> int:
    return len(questoes) + 1


'''
Ao usarmos o verbo PUT na url 
/autoteste/questao/<int:q_id>/erradas

queremos adicionar mais alternativas erradas à questão.

enviamos, no corpo do request, uma lista de alternativas 
incorretas, e elas devem ser acrescentadas à questão.

por exemplo:
    {"erradas":[1,2,3,4,5]}

Se a questao não existir, devemos retornar o codigo 404
e uma mensagem de erro

Se a questão existir, devemos retornar a questao modificada
'''


@app.route('/autoteste/questao/<int:q_id>/erradas', methods=['PUT'])
def add_wrong_answers(q_id):
    questao = get_questao(q_id)
    if not questao:
        return {"erro": "Questao nao encontrada"}, 404

    wrong_answers = request.json

    if not wrong_answers.get("erradas"):
        return {"erro": 'Campo [erradas] nao enviado'}, 400

    add_answers(questao, wrong_answers, "erradas")

    return jsonify(questoes[q_id]), 200


'''


faça o mesmo, adicionando alternativas corretas extras
'''


@app.route('/autoteste/questao/<int:q_id>/corretas', methods=['PUT'])
def add_correct_answers(q_id):
    questao = get_questao(q_id)
    if not questao:
        return {"erro": "Questao nao encontrada"}, 404

    correct_answers = request.json

    if not correct_answers.get("corretas"):
        return {"erro": 'Campo [corretas] nao enviado'}, 400

    add_answers(questao, correct_answers, "corretas")

    return jsonify(questoes[q_id]), 200


def add_answers(questao: dict, answers: list, tipo) -> None:
    for answer in answers[tipo]:
        if not answer_in_answers(answer, questao[tipo]):
            questao[tipo].append(answer)
    inx = questoes.index(questao)
    questoes[inx].update(questao)


'''
Agora melhore suas funções de adição de alternativas,
fazendo com que nao sejam adicionadas alternativas repetidas
'''


def answer_in_answers(answer, possible_answers) -> bool:
    if isinstance(answer, str):
        answer = answer.lower()

    for possible_answer in possible_answers:
        if isinstance(possible_answer, str):
            possible_answer = possible_answer.lower()
        if answer == possible_answer:
            return True
    return False


'''
Respondendo às perguntas

Fazendo um PUT na URL /autoteste/responder/1
o usuario 'fulano' pode responder à pergunta de id 1

ele deve mandar um json como o seguinte:
    { "usuario": "fulano",
      "resposta": "Remote Procedure Call"}
(o número da pergunta nao aparece no dicionario porque
já está na URL)

A sua resposta deve ser armazenada no dicionario respostas

Relembrando:
respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
é um dicionario, cada pessoa é uma chave
o valor da pessoa é um dicionário
(o valor do maria é {1:'Remote Procedure Call', 2: 64})
olhando para esse dicionario, associado a maria, temos 2
chaves, uma para cada pergunta que ela respondeu.
O valor associado a chave 1 é a resposta que maria deu
para a pergunta 1

Se o usuário ja respondeu a pergunta, devemos retornar um erro 
descritivo e o codigo 409 (confito de edição)

Se ele respondeu com uma alternativa que nao está
nem na lista de corretas nem na lista de incorretas
, devemos retornar
um erro descritivo e o codigo 400 (bad request)

Se o usuário nao está na lista de respostas, devemos adicionar
ele (podemos criar um usuário novo ao enviar uma resposta!)
'''


@app.route('/autoteste/responder/<int:q_id>', methods=['PUT'])
def send_answer(q_id):
    answer = request.json

    if not answer.get("usuario"):
        return {"erro": 'Campo [usuario] nao enviado'}, 400
    if not answer.get("resposta"):
        return {"erro": 'Campo [resposta] nao enviado'}, 400

    if answer["usuario"] not in respostas:
        respostas[answer["usuario"]] = {q_id: answer["resposta"]}
        return jsonify(answer), 200

    respostas_usuario = respostas[answer["usuario"]]
    if q_id in respostas_usuario:
        return {"erro": 'Pergunta já respondida pelo usuário'}, 409

    questao = get_questao(q_id)
    if not questao:
        return {"erro": "Questao nao encontrada"}, 404

    erradas = questao["erradas"]
    corretas = questao["corretas"]
    if not answer_in_answers(answer["resposta"], erradas) and not answer_in_answers(answer["resposta"], corretas):
        return {"erro": 'Resposta nao cadastrada nesta pergunta'}, 400

    respostas[answer["usuario"]].update({q_id: answer["resposta"]})

    return jsonify(respostas[answer["usuario"]]), 200


'''
O usuario deve poder ver quantas perguntas ainda nao
respondeu, quantas acertou e quantas errou.

Acessando a url /autoteste/<username>/resultados com o verbo GET
O usuario deve receber um json como o seguinte:

    {
    "usuario": "fulano",
    "acertos": 3,
    "erros": 2,
    "nao respondidas": 2
    }

Por exemplo, se acessarmos a url /autoteste/maria/resultados,
devemos receber

    {
    "usuario": "maria",
    "acertos": 2,
    "erros": 0,
    "nao respondidas": 0
    }


ja vimos urls como /aluno/<int:id_aluno>
Agora, estamos recebendo uma string em vez de uma id.
Para isso, é só escrever /autoteste/<nome_aluno>/resultados no app.route
'''


@app.route('/autoteste/<username>/resultados', methods=['GET'])
def results(username):
    if username not in respostas:
        return {"erro": 'Usuário nao encontrado'}, 404

    correct_answers = 0
    wrong_answers = 0
    missing_answers = 0

    respostas_usuario = respostas[username]

    for questao in questoes:
        if questao["id"] not in respostas_usuario.keys():
            missing_answers += 1
            continue

        if answer_in_answers(respostas_usuario[questao["id"]], questao["corretas"]):
            correct_answers += 1
        elif answer_in_answers(respostas_usuario[questao["id"]], questao["erradas"]):
            wrong_answers += 1

    result = {
        "usuario": username,
        "acertos": correct_answers,
        "erros": wrong_answers,
        "nao respondidas": missing_answers
    }

    return jsonify(result), 201


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(debug=True, host='0.0.0.0', port=5004)
