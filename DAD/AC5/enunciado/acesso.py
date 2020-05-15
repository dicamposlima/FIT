import requests


def leciona(id_professor: int, id_disciplina: int):
    try:
        result = requests.get(f'http://localhost:5000/leciona/{id_professor}/{id_disciplina}/')
    except requests.exceptions.RequestException:
        return 'Professor invalido', 500
    response = result.json()
    return (False, 'inexistente') if not response['response'] else response['leciona']


def aluno(nome_aluno: str):
    try:
        result = requests.get(f'http://localhost:5000/notas/{nome_aluno}/')
    except requests.exceptions.RequestException:
        return 'Aluno invalido', 500
    response = result.json()
    return (False, 'inexistente') if not response['response'] else response['aluno']
