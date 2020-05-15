from typing import List

from acesso import leciona, aluno
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'crie um app de todo em flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },

    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    },

]


@app.route('/')
def index():
    return "Sistema de entrega de atividades"


@app.route('/atividades/ver_tudo/', methods=['GET'])
def get_all():
    return jsonify(atividades)


@app.route('/atividade/<int:id_atividade>/')
def get_atividade(id_atividade: int):
    id_professor = None
    if "id_professor" in request.args:
        id_professor = int(request.args["id_professor"])
    for atividade in atividades:
        if id_atividade == int(atividade['id_atividade']):
            atividade_copy = {**atividade, 'url': f'/atividade/{id_atividade}/'}
            if id_professor:
                result = leciona(id_professor, int(atividade_copy['id_disciplina']))
                if isinstance(result, bool) and result:
                    return jsonify({'response': True, 'atividade': atividade_copy}), 200
            del atividade_copy['respostas']
            return jsonify({'response': True, 'atividade': atividade_copy}), 200
    return jsonify({'response': False, 'error': 'atividade nao encontrada'}), 404


@app.route('/notas/<nome_aluno>')
def notas(nome_aluno: str):
    result = aluno(nome_aluno)
    if isinstance(result, tuple):
        status, _ = result
        return (jsonify({'response': False}), 404) if not status else (status, 500)
    notas_aluno: List[int] = []
    for atividade in atividades:
        for resposta in atividade['respostas']:
            if result['id_aluno'] == resposta['id_aluno'] and 'nota' in resposta:
                notas_aluno.append(int(resposta['nota']))
                break
        else:
            notas_aluno.append(0)
    return jsonify({'response': True, 'notas': notas_aluno}), 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5050)
