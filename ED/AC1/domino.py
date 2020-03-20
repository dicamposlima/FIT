
'''
No fim do arquivo, temos uma classe para representar peças de dominó
Veja como a classe funciona:
   > peca = Domino(2,3)
   > peca.direita
   3
   > peca.esquerda
   2
   > peca
   |2|3|
   > peca.inverte()
   > peca
   |3|2|
   > peca.esquerda
   3
'''

'''
Crie uma funcao "nro direita" que recebe uma peça de dominó e retorna
o número da direita da peça
'''
def nro_direita(peca):
    return peca.direita

'''
Crie uma funcao peca_valida que recebe uma peça de dominó e verifica
se ambas os lados são válidos. Cada lado tem que ser um número, e 
só pode ser 1,2,3,4,5 ou 6
'''
def peca_valida(peca):
    lados = [1,2,3,4,5,6]
    return False if peca.direita not in lados else False if peca.esquerda not in lados else True

'''
Crie uma funcao "encaixa" que verifica se duas peças de dominó "encaixam".
Ou seja, posso colocar a peça2 logo depois da peça1, sem ter que virar
nenhuma das duas? Sua funcao deve retornar True se as peças encaixam,
false caso contrário.
'''
def encaixa(peca1,peca2):
    return peca1.direita == peca2.esquerda

'''
Crie uma função "encaixa_de_algum_jeito" que recebe duas peças de dominó
e verifica se existe alguma maneira de encaixar elas, girando as peças se
necessário
'''
def encaixa_de_algum_jeito(peca1,peca2):
    return peca1.esquerda == peca2.esquerda or peca1.direita == peca2.direita or peca1.esquerda == peca2.direita or peca1.direita == peca2.esquerda

'''
Crie uma funcao "encaixa_girando_so_a_segunda" que pode girar (ou nao)
a segunda peça pra encaixar. 

Ela tenta colocar primeiro a peca1, depois a peca2 (girada ou nao)
, mas não gira a primeira

Retorna True se encaixa
'''
def encaixa_girando_so_a_segunda(peca1,peca2):
    return peca1.direita == peca2.esquerda or peca1.direita == peca2.direita

'''
Agora, vamos começar a pensar em jogos de dominó.
Um jogo é uma lista de dominós que se encaixam (na posicao atual,
sem precisar girar).

Repetindo: todos se encaixam. O dominó 0 se encaixa com o 1,
o 1 com o 2, e assim até o domino len(lista)-2, que se encaixa com o
len(lista)-1

Crie uma funçao jogo_valido que recebe uma lista de dominós
e retorna True se a lista representa um jogo valido (False caso
contrário)
'''
def jogo_valido(jogo):
    jogo_len = len(jogo)
    if jogo_len <= 1:
        return True
    increment = 0
    while increment < (jogo_len-1):
        if jogo[increment].direita != jogo[increment+1].esquerda:
            return False
        increment = increment + 1
    return True

'''
Crie uma funcao ciclo_valido, que recebe uma lista como acima, e se 
certifica, como acima, que o dominó 0 encaixa com o 1, e o 1 com o 2
e assim por diante.

A diferenca é que devemos receber dessa vez um ciclo. O último dominó
um número "livre". Esse número "livre" deve se encaixar com o número livre
do primeiro.
'''
def ciclo_valido(jogo):
    jogo_len = len(jogo)
    return jogo_valido(jogo) and jogo[0].esquerda == jogo[jogo_len-1].direita

'''
Agora, vamos fingir que somos um jogador. Ele vê o jogo na mesa,
e tenta encaixar uma de suas peças.

Escreva uma funcao jogador, que recebe um jogo e uma peça
solta, e retorna a string 'atras' se a peça encaixa atrás,
'frente' se ela encaixa na frente, e False se ela não encaixa

Se for necessário, você pode girar a peça para encaixar
'''

def jogador(jogo,peca):
    jogo_len = len(jogo)
    return 'atras' if jogo[0].esquerda == peca.direita or jogo[0].esquerda == peca.esquerda else 'frente' if jogo[jogo_len-1].direita == peca.direita or jogo[jogo_len-1].direita == peca.esquerda else False
   

'''
Já aprendemos a verificar se um jogo está OK. Agora, devemos
aprender a montar um jogo.

Antes disso, devemos aprender a colocar itens em uma lista, tanto
no começo quanto no final

Veja o exemplo:
   > lista = [1,2,3]
   > lista.insert(0,'comeco')
   > lista.append('final')
   > lista
   ['comeco', 1, 2, 3, 'final']
'''

'''
Faça uma função no_comeco que recebe uma lista representando um jogo válido
e uma peça que encaixa no começo do jogo.

Ela deve colocar a peça no começo do jogo e retornar o novo jogo
'''
def no_comeco(jogo,peca):
    return jogo.insert(0, peca)

'''
Façamos uma função jogo_grande que recebe uma lista de dominós (fora de ordem)
e vai montando um jogo com a lista de dominós.

A idéia é montar um jogo válido, de forma que nenhum dos dominós "sobrando"
se encaixe (montar um jogo "travado", que não dá pra aumentar sem mexer nas 
peças já colocadas)

Tire as peças que você usar da lista de dominós

Retorne seu jogo válido e a lista de peças que sobraram

DICA: voce pode ir verificando se existe um dominó que ainda encaixa.
Se existe, voce insere e começa a verificar de novo.
Se não existe, voce achou uma solução do jeito que tinha sido pedido

def encaixa(peca1,peca2):
    return peca1.direita == peca2.esquerda
def encaixa_de_algum_jeito(peca1,peca2):
    return peca1.esquerda == peca2.esquerda or peca1.direita == peca2.direita or peca1.esquerda == peca2.direita or peca1.direita == peca2.esquerda
def encaixa_girando_so_a_segunda(peca1,peca2):
    return peca1.direita == peca2.esquerda or peca1.direita == peca2.direita
def jogador(jogo,peca):

'''
def jogo_grande(pecas):
    jogo_grande = []
    pecas_sobrando = []
    no_comeco(jogo_grande, pecas.pop(0))
    while len(pecas) > 0:
        if jogador(jogo_grande, pecas[0]) == 'atras':
            if encaixa(jogo_grande[0], pecas[0]):
                peca_invertida = pecas.pop(0).inverte
                no_comeco(jogo_grande, peca_invertida)
            else:
                no_comeco(jogo_grande, pecas.pop(0))
        elif jogador(jogo_grande, pecas[0]) == 'frente':
            if encaixa(jogo_grande[len(jogo_grande)-1], pecas[0]):
                jogo_grande.append(pecas.pop(0))
            else:
                peca_invertida = pecas.pop(0).inverte
                jogo_grande.append(peca_invertida)
        else:
            pecas_sobrando.append(pecas.pop(0))
    return jogo_grande,pecas_sobrando

 
import unittest
class TestClientes(unittest.TestCase):
    def test_01_direita(self):
        self.assertEqual(nro_direita(Domino(2,5)), 5)
        self.assertEqual(nro_direita(Domino(1,5)), 5)
        self.assertEqual(nro_direita(Domino(1,3)), 3)
        self.assertEqual(nro_direita(Domino(4,1)), 1)

    def test_02_peca_valida(self):
        self.assertTrue(peca_valida(Domino(2,5)))
        self.assertFalse(peca_valida(Domino(8,5)))
        self.assertTrue(peca_valida(Domino(5,2)))
        self.assertFalse(peca_valida(Domino(-1,5)))
        self.assertTrue(peca_valida(Domino(1,1)))
        self.assertFalse(peca_valida(Domino(2.3,5)))
        self.assertTrue(peca_valida(Domino(1,2)))
   
    def test_03_encaixa(self):
        self.assertTrue (encaixa(Domino(2,5),Domino(5,3)))
        self.assertFalse(encaixa(Domino(2,5),Domino(3,5)))
        self.assertFalse(encaixa(Domino(5,2),Domino(5,3)))
        self.assertFalse(encaixa(Domino(5,2),Domino(3,5)))
        self.assertFalse(encaixa(Domino(1,2),Domino(3,4)))
    
    def test_04_encaixa_de_algum_jeito(self):
        self.assertTrue (encaixa_de_algum_jeito(Domino(2,5),Domino(5,3)))
        self.assertTrue (encaixa_de_algum_jeito(Domino(2,5),Domino(3,5)))
        self.assertTrue (encaixa_de_algum_jeito(Domino(5,2),Domino(5,3)))
        self.assertTrue (encaixa_de_algum_jeito(Domino(5,2),Domino(3,5)))
        self.assertFalse(encaixa_de_algum_jeito(Domino(1,2),Domino(3,4)))
    
    def test_05_encaixa_girando_segunda(self):
        self.assertTrue (encaixa_girando_so_a_segunda(Domino(2,5),Domino(5,3)))
        self.assertTrue (encaixa_girando_so_a_segunda(Domino(2,5),Domino(3,5)))
        self.assertFalse(encaixa_girando_so_a_segunda(Domino(5,2),Domino(5,3)))
        self.assertFalse(encaixa_girando_so_a_segunda(Domino(5,2),Domino(3,5)))
        self.assertFalse(encaixa_girando_so_a_segunda(Domino(1,2),Domino(3,4)))

    def test_06_jogo_valido(self):
        self.assertTrue(jogo_valido([Domino(2,5)]))
        self.assertTrue(jogo_valido([Domino(2,5),Domino(5,2)]))
        self.assertTrue(jogo_valido([Domino(2,5),Domino(5,3),Domino(3,4)]))
        self.assertTrue(jogo_valido([Domino(2,5),Domino(5,3),Domino(3,4),Domino(4,4)]))
        self.assertFalse(jogo_valido([Domino(2,5),Domino(3,5),Domino(3,4),Domino(4,3)]))
        self.assertFalse(jogo_valido([Domino(2,5),Domino(3,4),Domino(4,3)]))
    
    def test_07_ciclo_valido(self):
        self.assertFalse(ciclo_valido([Domino(2,5)]))
        self.assertTrue(ciclo_valido([Domino(2,5),Domino(5,2)]))
        self.assertFalse(ciclo_valido([Domino(2,5),Domino(5,3),Domino(3,4)]))
        self.assertTrue(ciclo_valido([Domino(6,5),Domino(5,3),Domino(3,6)]))
        self.assertFalse(ciclo_valido([Domino(2,5),Domino(5,3),Domino(3,4),Domino(4,4)]))
        self.assertFalse(ciclo_valido([Domino(2,5),Domino(3,5),Domino(3,4),Domino(4,3)]))
        self.assertFalse(ciclo_valido([Domino(2,5),Domino(3,4),Domino(4,3)]))

    def test_08_jogador(self):
        self.assertEqual(jogador([Domino(2,5)],Domino(2,3)),'atras')
        self.assertEqual(jogador([Domino(2,5)],Domino(5,3)),'frente')
        self.assertEqual(jogador([Domino(2,5),Domino(5,3),Domino(3,4)],
                                  Domino(2,3)),'atras')
        self.assertEqual(jogador([Domino(2,5),Domino(5,3),Domino(3,4)],
                                  Domino(4,3)),'frente')
        self.assertEqual(jogador([Domino(2,5),Domino(5,3),Domino(3,4)],
                                  Domino(5,1)),False)

    def test_09_no_comeco(self):
        jogo = [Domino(2,3)]
        no_comeco(jogo,Domino(1,2))
        self.assertEqual(jogo[0],Domino(1,2))
        self.assertEqual(len(jogo),2)
        no_comeco(jogo,Domino(3,1))
        self.assertEqual(jogo[0],Domino(3,1))
        self.assertEqual(len(jogo),3)

    def test_10_jogo_grande(self):
        resposta, sobrou = jogo_grande([
                    Domino(1,2),
                    Domino(2,3),
                    Domino(3,4),
                    Domino(4,5),
                    Domino(5,6),
                    Domino(6,1)])
        self.assertEqual(self.jogo_valido(resposta),True)
        self.assertEqual(sobrou,[])
        resposta, sobrou = jogo_grande([
                    Domino(1,2),
                    Domino(2,3),
                    Domino(3,4),
                    Domino(4,4),
                    Domino(6,6)])
        self.assertEqual(self.jogo_valido(resposta),True)
        if sobrou != [Domino(6,6)] and sobrou != [ 
                         Domino(1,2), Domino(2,3), Domino(3,4),
                         Domino(4,4), ]:
                              self.fail('o conjunto de pecas sobrando nao esta ok. Leia o teste (o erro deve ter te dito a linha)')

    
    def jogo_valido(self,jogo):
        for num,peca in enumerate(jogo):
            if num != 0 and peca.esquerda != jogo[num-1].direita:
                return False
        return True


       
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

'''
classe para representar peças de dominó
'''


class Domino():
    def __init__(self,esquerda,direita):
        self.esquerda = esquerda
        self.direita = direita

    def inverte(self):
        v1 = self.esquerda
        v2 = self.direita
        self.esquerda = v2
        self.direita = v1

    #pra imprimir bonito
    def __repr__(self):
        return '|'+str(self.esquerda)+'|'+str(self.direita)+'|' 
    #pra igualdade funcionar bem
    def __eq__(self,other):
        return self.esquerda == other.esquerda and self.direita == other.direita

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()

