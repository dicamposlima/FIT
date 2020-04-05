from flask import Flask, jsonify, request
from requests import api

app = Flask(__name__) 

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

site = "http://localhost:5002"

# GERAL
@app.route("/show")
def all(): 
    return jsonify(database)

@app.route('/reseta', methods=['POST'])
def reseta():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return jsonify(database)

# ALUNOS
@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.json
    
    if not novo_aluno.get("nome"):
        return {"status":400, "erro":'aluno sem nome'}, 400

    id = novo_aluno.get("id")
    aluno = api.get(f"{site}/alunos/{id}")
    if aluno.status_code == 400:
        database['ALUNO'].append(novo_aluno)
        return jsonify(database['ALUNO'])
    return {"status":400, "erro":'id ja utilizada'}, 400

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    novo_nome = request.json

    aluno = api.get(f"{site}/alunos/{id_aluno}")
    if aluno.status_code == 400:
        return {"status":400, "erro":'aluno nao encontrado'}, 400

    if not novo_nome.get("nome"):
        return {"status":400, "erro":'aluno sem nome'}, 400

    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            aluno["nome"] = novo_nome.get("nome")
            return jsonify(database['ALUNO'])
    return {"status":400, "erro":'aluno nao encontrado'}, 400

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
    aluno = api.get(f"{site}/alunos/{id_aluno}")
    if aluno.status_code == 400:
        return {"status":400, "erro":'aluno nao encontrado'}, 400

    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return {"status":400, "erro":'aluno nao encontrado'}, 400

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return {"status":400, "erro":'aluno nao encontrado'}, 400

# PROFESSORES
@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.json
    
    if not novo_professor.get("nome"):
        return {"status":400, "erro":'professor sem nome'}, 400

    id = novo_professor.get("id")
    professor = api.get(f"{site}/professores/{id}")
    if professor.status_code == 400:
        database['PROFESSOR'].append(novo_professor)
        return jsonify(database['PROFESSOR'])
    return {"status":400, "erro":'id ja utilizada'}, 400

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def edita_professor(id_professor):
    novo_nome = request.json
    
    professor = api.get(f"{site}/professores/{id_professor}")
    if professor.status_code == 400:
        return {"status":400, "erro":'professor nao encontrado'}, 400

    if not novo_nome.get("nome"):
        return {"status":400, "erro":'professor sem nome'}, 400
    
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            professor["nome"] = novo_nome.get("nome")
            return jsonify(database['PROFESSOR'])
    return {"status":400, "erro":'professor nao encontrado'}, 400

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    professor = api.get(f"{site}/professores/{id_professor}")
    if professor.status_code == 400:
        return {"status":400, "erro":'professor nao encontrado'}, 400

    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            database['PROFESSOR'].remove(professor)
            return jsonify(database['PROFESSOR'])
    return {"status":400, "erro":'professor nao encontrado'}, 400

@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return jsonify(professor)
    return {"status":400, "erro":'professor nao encontrado'}, 400

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True) 