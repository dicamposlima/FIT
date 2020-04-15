from flask import Flask, jsonify, request
from requests import api

app = Flask(__name__) 

database = {}
database["PESSOA"] = []

site = "http://localhost:5003"

# GERAL
def get_pessoa(pessoa_id: int) -> list:
    try:
        for pessoa in database["PESSOA"]:
            if int(pessoa['id']) == pessoa_id:
                return pessoa
        else:
            return []
    except Exception as erro:
        raise

@app.route('/reseta', methods=['POST'])
def reseta():
    database["PESSOA"] = []
    return jsonify(database)

# PESSOAS
@app.route('/pessoas')
def pessoas():
    return jsonify(database["PESSOA"])

@app.route('/pessoas', methods=['POST'])
def nova_pessoa():
    nova_pessoa = request.json
    
    if not nova_pessoa.get("nome"):
        return {"status":400, "erro":'pessoa sem nome'}, 400

    id = nova_pessoa.get("id")
    pessoa = api.get(f"{site}/pessoas/{id}")
    if pessoa.status_code == 400:
        database["PESSOA"].append(nova_pessoa)
        return jsonify(database["PESSOA"])
    return {"status":400, "erro":'id ja utilizada'}, 400

@app.route('/pessoas/<int:ia_pessoa>', methods=['PUT'])
def edita_pessoa(ia_pessoa):
    novo_nome = request.json

    pessoa = api.get(f"{site}/pessoas/{ia_pessoa}")
    if pessoa.status_code == 400:
        return {"status":400, "erro":'pessoa nao encontrado'}, 400

    if not novo_nome.get("nome"):
        return {"status":400, "erro":'pessoa sem nome'}, 400

    pessoa = get_pessoa(ia_pessoa)
    if pessoa:
        pessoa["nome"] = novo_nome.get("nome")
        return jsonify(database["PESSOA"])
    return {"status":400, "erro":'pessoa nao encontrado'}, 400

@app.route('/pessoas/<int:ia_pessoa>', methods=['DELETE'])
def deleta_pessoa(ia_pessoa):
    pessoa = api.get(f"{site}/pessoas/{ia_pessoa}")
    if pessoa.status_code == 400:
        return {"status":400, "erro":'pessoa nao encontrado'}, 400
    
    pessoa = get_pessoa(ia_pessoa)
    if pessoa:
        database["PESSOA"].remove(pessoa)
        return jsonify(database["PESSOA"])
    return {"status":400, "erro":'pessoa nao encontrado'}, 400

@app.route('/pessoas/<int:ia_pessoa>', methods=['GET'])
def localiza_pessoa(ia_pessoa):
    pessoa = get_pessoa(ia_pessoa)
    if pessoa:
        return jsonify(pessoa)
    return {"status":400, "erro":'pessoa nao encontrado'}, 400

@app.route('/sinalizar_interesse/<int:ia_pessoa_1>/<int:ia_pessoa_2>/', methods=['PUT'])
def sinaliza_interesse(ia_pessoa_1, ia_pessoa_2):
    
    pessoa1 = api.get(f"{site}/pessoas/{ia_pessoa_1}")
    if pessoa1.status_code == 400:
        return {"status":404, "erro":'pessoa nao encontrado'}, 404
    
    pessoa2 = api.get(f"{site}/pessoas/{ia_pessoa_2}")
    if pessoa2.status_code == 400:
        return {"status":404, "erro":'pessoa nao encontrado'}, 404
    
    pessoa1 = get_pessoa(ia_pessoa_1)
    pessoa2 = get_pessoa(ia_pessoa_2)

    if pessoa2.get("sexo") and pessoa1.get("buscando") and pessoa2["sexo"] not in pessoa1["buscando"]:
        return {"status":400, "erro":'interesse incompativel'}, 400
    
    if pessoa2.get('matches'):
        pessoa2['matches'].append(ia_pessoa_1)
    else:
        pessoa2['matches'] = [ia_pessoa_1]
   
    return "sinaliza_interesse", 200

@app.route('/matches/<int:ia_pessoa>', methods=['GET'])
def matches(ia_pessoa):
    
    pessoa = api.get(f"{site}/pessoas/{ia_pessoa}")
    if pessoa.status_code == 400:
        return {"status":404, "erro":'pessoa nao encontrado'}, 404
    
    pessoa = get_pessoa(ia_pessoa) 
    matches = pessoa['matches'] if pessoa.get('matches') else []

    return jsonify(matches), 200


@app.route('/sinalizar_interesse/<int:ia_pessoa_1>/<int:ia_pessoa_2>/', methods=['DELETE'])
def remove_interesse(ia_pessoa_1, ia_pessoa_2):
    
    pessoa1 = api.get(f"{site}/pessoas/{ia_pessoa_1}")
    if pessoa1.status_code == 400:
        return {"status":404, "erro":'pessoa nao encontrado'}, 404
    
    pessoa2 = api.get(f"{site}/pessoas/{ia_pessoa_2}")
    if pessoa2.status_code == 400:
        return {"status":404, "erro":'pessoa nao encontrado'}, 404
    
    pessoa = get_pessoa(ia_pessoa_2)    
    if pessoa.get('matches'):
        pessoa['matches'].remove(ia_pessoa_1)
   
    return "remove_interesse", 200



if __name__ == '__main__':
    app.run(host = 'localhost', port = 5003, debug = True) 