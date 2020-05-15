import requests
import acesso

import unittest


class TestStringMethods(unittest.TestCase):

    def test_000_leciona(self):
        r = requests.get('http://localhost:5000/leciona/1/1/')
        self.assertEqual(r.json(), {'leciona': True, 'response': True})
        r = requests.get('http://localhost:5000/leciona/100/1/')
        self.assertEqual(r.json(), {'leciona': False, 'response': True})

    def test_001_leciona_not_found(self):
        r = requests.get('http://localhost:5000/leciona/1/100/')
        self.assertEqual(r.json()['response'], False)
        self.assertEqual(r.json(), {'response': False, 'error': 'disciplina nao encontrada'})
        self.assertEqual(r.status_code, 404)

    def test_002_metodo_leciona(self):
        self.assertEqual(acesso.leciona(1, 1), True)
        self.assertEqual(acesso.leciona(100, 1), False)
        self.assertEqual(acesso.leciona(1, 200), (False, 'inexistente'))

    def test_003_atividade(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um app de todo em flask")
        self.assertEqual(r.json()['response'], True)
        r = requests.get('http://localhost:5050/atividade/2/')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um servidor que envia email em Flask")

    def test_004_atividade_not_found(self):
        r = requests.get('http://localhost:5050/atividade/123/')
        self.assertEqual(r.json()['response'], False)
        self.assertEqual(r.status_code, 404)

    def test_005_atividade_url(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertEqual(r.json()['response'], True)
        # quero a URL na resposta
        self.assertEqual(r.json()['atividade']['url'], '/atividade/1/')
        r = requests.get('http://localhost:5050/atividades/ver_tudo/')
        self.assertEqual('enunciado' in r.json()[0], True)
        # mas sem mudar o valor na estrutura de dados do servidor
        self.assertEqual('url' in r.json()[0], False)

    def test_006_atividade_professor(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertFalse('respostas' in r.json()['atividade'])
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=100')
        # mais certo seria usar a linha abaixo, mas fiz desse jeito mais simples pra
        # ficar mais claro pra voces qual era a URL
        # r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':100})
        self.assertFalse('respostas' in r.json()['atividade'])
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=1')
        # mais certo seria usar a linha abaixo, mas fiz desse jeito mais simples pra
        # ficar mais claro pra voces qual era a URL
        # r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':1})
        self.assertTrue('respostas' in r.json()['atividade'])

    def test_007_alunos_e_notas(self):
        r = requests.get('http://localhost:5050/notas/janaina')
        notas = r.json()['notas']
        self.assertEqual(notas, [0, 0])
        r = requests.get('http://localhost:5050/notas/cicero')
        notas = r.json()['notas']
        self.assertEqual(notas, [10, 10])
        r = requests.get('http://localhost:5050/notas/alexandre')
        notas = r.json()['notas']
        # self.assertEqual(notas, [9,0])
        # queria ter escrito o assert acima, mas vai que voce me devolve em outra ordem?
        self.assertIn(9, notas)
        self.assertIn(0, notas)

    def test_007a_alunos_e_notas(self):
        r = requests.get('http://localhost:5050/notas/miguel')
        notas = r.json()['notas']
        self.assertEqual(notas, [0, 0])
        self.assertEqual(r.json()['response'], True)

    def test_007b_alunos_e_notas_aluno_inexistente(self):
        r = requests.get('http://localhost:5050/notas/diana')
        self.assertEqual(r.json()['response'], False)
        self.assertEqual(r.status_code, 404)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


runTests()
