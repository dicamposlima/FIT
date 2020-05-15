from flask import Flask, jsonify

app = Flask(__name__)
professores = [
    {'nome': "joao", 'id_professor': 1},
    {'nome': "jose", 'id_professor': 2},
    {'nome': "maria", 'id_professor': 3}
]

alunos = [
    {'nome': "alexandre", 'id_aluno': 1},
    {'nome': "miguel", 'id_aluno': 2},
    {'nome': "janaina", 'id_aluno': 3},
    {'nome': "cicero", 'id_aluno': 4},
]

disciplinas = [
    {'nome': "distribuidos", 'id_disciplina': 1, 'alunos': [1, 2], 'professores': [1], 'publica': False},
    {'nome': "matematica financeira", 'id_disciplina': 2, 'alunos': [2], 'professores': [3], 'publica': True},
    {'nome': "matematica basica", 'id_disciplina': 3, 'alunos': [1, 2], 'professores': [3, 2], 'publica': False}

]


@app.route('/')
def index():
    return "Sistema de controle de pessoas"


@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
    return jsonify([professores, alunos, disciplinas])


@app.route('/leciona/<int:id_professor>/<int:id_disciplina>/')
def leciona(id_professor: int, id_disciplina: int):
    for disciplina in disciplinas:
        if id_disciplina == int(disciplina['id_disciplina']):
            if id_professor in disciplina['professores']:
                return jsonify({'response': True, 'leciona': True}), 200
            return jsonify({'response': True, 'leciona': False}), 200
    return jsonify({'response': False, 'error': 'disciplina nao encontrada'}), 404


@app.route('/notas/<nome_aluno>/')
def notas(nome_aluno: str):
    for aluno in alunos:
        if nome_aluno == aluno['nome']:
            return jsonify({'response': True, 'aluno': aluno}), 200
    return jsonify({'response': False, 'error': 'aluno nao encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
