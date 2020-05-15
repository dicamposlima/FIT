

from jogadores_select import JogadorNaoExisteException
from jogadores_select import conta_jogadores
from jogadores_select import consultar_jogador
from jogadores_select import consultar_jogador_por_email as jogador_por_email
'''

Examine as funcoes do arquivo jogadores_select.py, que ilustra como
podemos usar o sql no python com sqlite.

(depois faça várias atividades e depois volte aqui)

Examine as funcoes do jogadores.py, que mostra como fazer alteracoes
no banco usando a biblioteca sqlite

'''
from jogadores_alteracoes import criar_jogador
from jogadores_alteracoes import alterar_jogador
from jogadores_alteracoes import remover_jogador


'''
Inicio dos testes
'''

import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_01_jogador_por_id(self):
        self.assertEqual(consultar_jogador(1)[1],'lucas goncalves')
        self.assertEqual(consultar_jogador(2)[1],'victor')
        self.assertRaises(JogadorNaoExisteException,consultar_jogador,567)


    def test_02_contar_jogadores(self):
        self.assertEqual(conta_jogadores(),3)
    
    def test_03_jogador_por_email(self):
        self.assertEqual(jogador_por_email('lucas.goncalves@faculdadeimpacta.com.br')['nome'],'lucas goncalves')
        self.assertEqual(jogador_por_email('victor.silva@faculdadeimpacta.com.br')['nome'],'victor')
        self.assertRaises(JogadorNaoExisteException,jogador_por_email,'john@doe')


    def test_04_criar_jogadores(self):
        criar_jogador('macaco louco','macaco@superpoderosas.com')
        self.assertEqual(conta_jogadores(),4)
        self.assertEqual(jogador_por_email('macaco@superpoderosas.com')['nome'],
                         'macaco louco')


    def test_05_alterar_jogadores(self):
        novo_victor = {'email': 'victor.silva@faculdadeimpacta.com.br',
                        'nome': 'victor silva'}
        alterar_jogador(2,novo_victor)
        self.assertEqual(consultar_jogador(2)[1],'victor silva')
    
    def test_06_excluir_jogadores(self):
        criar_jogador('homem codorna','doug@funny.com')
        self.assertEqual(jogador_por_email('doug@funny.com')['nome'],
                         'homem codorna')
        remover_jogador(5)
        self.assertRaises(JogadorNaoExisteException,jogador_por_email,'doug@funny.com')
    
import shutil
def runTests():
        shutil.copyfile('rpg.original.db','rpg.db')
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
