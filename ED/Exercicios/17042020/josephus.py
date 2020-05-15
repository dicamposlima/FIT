'''
EXPLICACAO

    Uma fila é um tipo abstrato de dados que suporta 2 operações
    basicas (e mais duas que vamos falar mais pra frente, mas
    sao bem mais simples).

    As duas operações basicas são "insere" e "retira"

    A idéia é que novos elementos são inseridos "no fim"
    da fila, e, se retiramos alguém, é o elemento
    mais antigo.

    Basicamente é uma fila de supermercado. Quem entra entra
    "no fim", quando vai sair alguém, sai o mais velho,
    que está "na frente".

    Ou seja: quem entrou primeiro sai primeiro. Em inglês,
    diriamos First In First Out, ou FIFO.

'''

'''
   EXEMPLO

   Comecemos com uma fila vazia: []
   insere(2)
   fila: [2]
   insere(5)
   fila: [2, 5]
   insere(1)
   fila: [2, 5, 1]
   retira()
   sai o 2
   fila: [5, 1]
'''

'''
Exercicio

Inicie com uma fila vazia.
Execute:
    insere(3)
    insere(4)
    insere(1)
    insere(2)

Qual o estado da fila?
Responda, em forma de lista, na variavel fila1
'''


fila1 = [3, 4, 1, 2]


'''
Exercicio

Inicie com uma fila vazia.
Execute:
    insere(3)
    insere(4)
    remove()
    insere(1)
    insere(2)
    remove()

Qual o estado da fila?
Responda, em forma de lista, na variavel fila2
'''


fila2 = [1, 2]


'''
Exercicio

Inicie com uma fila vazia.
Execute:
    insere(3)
    insere(4)
    remove()
    insere(1)
    remove()
    insere(2)
    remove()
    insere(7)

Qual o estado da fila?
Responda, em forma de lista, na variavel fila3
'''


fila3 = [2, 7]


'''

   Para implementar a idéia de filas em python, usamos uma lista.
   Para criar uma lista vazia, fazemos lista = []
   Para a operação "retira", fazemos lista.pop(0)
   Para adicionar o elemento "banana", fazemos lista.append('banana')

   Veja o exemplo a seguir

   > fila = []
   > fila.append(1)
   > fila
   [1]
   > fila.append(2)
   > fila
   [1, 2]
   > fila.append(3)
   > fila
   [1, 2, 3]
   > retirado = fila.pop(0)
   > fila
   [2, 3]
   > retirado
   1
   > fila.append(4)
   > fila
   [2, 3, 4]
   > retirado = fila.pop(0)
   > fila
   [3, 4]
   > retirado
   2
'''

'''
EXERCICIO

    Definindo uma fila como acima, com listas,
    faca uma funcao coloca_fila(fila,elemento)
    que adiciona o elemento à fila
'''


def coloca_fila(fila: list, elemento: int) -> list:
    fila.append(elemento)
    return fila

'''
EXERCICIO

    "faca uma funcao retira(fila)" que tira o elemento mais velho 
    da fila e o retorna.

    Ou seja:
    >fila = [10,2,3]
    >a = retira(fila)
    >a
    10 #o retorno foi 10, o primeiro da fila
    >fila
    [2,3] #esses sao os caras que ainda estao na fila

'''


def retira(fila: list) -> int:
    return fila.pop(0)

'''
EXPLICACAO

    Para verificar quantos elementos tem na fila, é só fazer len(fila).
    Veja o exemplo

    > fila = []
    > fila.append(2)
    > fila.append(3)
    > fila
    [2, 3]
    > len(fila)
    2
    > fila.append(4)
    > fila
    [2, 3, 4]
    > len(fila)
    3
    > retirar = fila.pop(0)
    > retirar
    2
    > fila
    [3, 4]
    > len(fila)
    2
'''


def tamanho(fila: list) -> int:
    return len(fila)


'''
EXERCICIO
Usando o tamanho, podemos definir uma funcao fila_vazia
que diz se a fila está vazia (len(fila) == 0) ou nao

Ela retorna True se a fila estiver vazia, False caso contrário
'''


def fila_vazia(fila: list) -> bool:
    return False if tamanho(fila) > 0 else True


'''
EXPLICACAO
    Para ver qual é o primeiro elemento da fila, sem retirar
    ninguém, é só usar o indice 0 

    >>> fila=[10,11,100,1]
    >>> fila[0] #consulta sem retirar
    10
    >>> fila.pop(0) #retira - altera a fila
    10
    >>> fila
    [11, 100, 1]
    >>> fila[0]
    11
    >>> fila[0]
    11
    >>> fila.pop(0)
    11
    >>> fila
    [100, 1]
    >>> fila[0]
    100
'''


def primeiro(fila: list) -> int:
    return fila[0]


'''
EXERCICIO

    faça uma funcao vira_1(fila) que recebe uma fila,
    pega o retira o primeiro elemento do começo da fila
    e coloca ele de volta, no fim da fila

    Ex:
    fila = [1,2,3]
    se fizermos vira_1(fila), a fila passa a ser [2,3,1]
'''


def vira_1(fila: list) -> list:
    primeiro_elemento = retira(fila)
    return coloca_fila(fila, primeiro_elemento)


'''
EXERCICIO

    faça uma funcao vira_5(fila) que recebe uma fila,
    pega o retira o primeiro elemento do começo da fila
    e coloca ele de volta, no fim da fila.
    Depois faz isso de novo, pegando o novo primeiro da fila
    e colocando no final
    Depois faz isso de novo... 
    Fazendo 5 vezes no total

    Ex: 
    fila = [1,2,3,4,5,6,7,8,9]
    #pega o 1 e colocou no comeco, depois o 2,
    #depois o 3, depois o 4, depois o 5.
    depois de vira_5(fila), a fila será [6,7,8,9,1,2,3,4,5]
'''


def vira_5(fila:list) -> list:
    return vira_n(fila, 5)


'''
EXERCICIO
    Faça uma funçao vira_n(fila,n), analoga a vira 5
    A idéia agora é que você pode especificar quantas
    vezes a operacao "pega do começo e poe no fim"
    acontece.

    Exemplo:
    fila = [1,2,3,4,5,6]
    depois de vira_n(fila,3), a fila será [4,5,6,1,2,3]
    se fizermos vira_n(fila,3) novamente, a fila será [1,2,3,4,5,6]
    se fizermos vira_n(fila,1), a fila será [2,3,4,5,6,1]
'''


def vira_n(fila: list, n: int) -> list:
    for vira in range(n):
        fila = vira_1(fila)
    return fila


'''
EXERCICIO
    Faça uma funçao vira_4_mata_1(fila),
    que faz o mesmo que vira_5 para os primeiros 4 elementos, 
    mas depois tira o primeiro elemento da fila 
    e nao coloca ele de volta
    
    Ex: 
    fila = [1,2,3,4,5,6,7,8,9]
    #pega o 1 e colocou no comeco, depois o 2,
    #depois o 3, depois o 4. Tira o 5 e nao coloca.
    depois de vira_4_mata_1(fila), a fila será [6,7,8,9,1,2,3,4]
    se fizemos vira_4_mata_1(fila) de novo, a fila será [2,3,4,6,7,8,9]
'''


def vira_4_mata_1(fila:list) -> int:
    fila = vira_n(fila, 4)
    return retira(fila)


'''
Exercicio
    Faça uma funcao fila_inicial(n) que recebe um numero n
    e retorna uma lista [1,2,3,...,n] (ou seja, uma lista
    dos numeros de 1 até n
'''


def fila_inicial(n:int) -> list:
    fila = range(1, n+1)
    return list(fila)


'''
EXPLICACAO
O problema de Josephus é assim conhecido por causa da lenda 
de Flavius Josephus, um historiador que viveu no século 1. 
Segundo o relato de Josephus do cerco de Yodfat, 
ele e seus companheiros (40 soldados) foram presos em uma caverna, 
cuja saída foi bloqueada pelos romanos. 

Eles preferiram suicidar-se a serem capturados, 
e decidiram que iriam formar um círculo e começar a matar-se 
pulando de três em três. 
Josephus afirma que, por sorte ou talvez pela mão de Deus, 
ele permaneceu por último e preferiu 
entregar-se aos romanos a suicidar-se.

Em cada caso de teste de entrada haverá um par de números 
inteiros positivos "pessoas" e "pulo". O  número "pessoas" representa 
a quantidade de pessoas no círculo, 
numeradas de 1 até n. 
O número "pulo" representa o tamanho do salto 
de um homem até o próximo homem que será morto.

Junto desse arquivo, há uma imagem fazendo um exemplo,
com 5 homens e pulo = 2

Neste exemplo o elemento que restará após as eliminações é 3. 
'''

'''
EXERCICIO
Faremos o seguinte: criaremos uma funcao josephus
que recebe 2 numeros: o numero de pessoas e o pulo.

Lembrando que as pessoas tem "nomes" 1,2,3..n, a funcao
deve retornar o numero do sobrevivente 

A ideia é fazer isso da seguinte forma:
    comece com uma lista de 1,2,3...n
    enquanto tem mais de uma pessoa na fila, vá retirando as pessoas pelo
    comeco da fila, e devolvendo no final

    controle quantas pessoas voce esta tirando, de forma que, quando tiver tirado
    "pulo" pessoas, voce nao insira essa pessoa de volta

    Existe um exemplo completo embaixo da funcao josephus
'''


def josephus(pessoas: int, pulo: int) -> int:
    fila = fila_inicial(pessoas)
    while tamanho(fila) > 1:
        fila = vira_n(fila, pulo-1)
        fila.pop(0)
    return fila.pop(0)


'''
exemplo completo: josephus(10,3)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (inicial)
pessoa = fila.pop(0) #tiro o 1 do começo
fila.append(pessoa) #e coloco no final
[2, 3, 4, 5, 6, 7, 8, 9, 10, 1] 
pessoa = fila.pop(0) #tiro o 2 do começo
fila.append(pessoa) #e coloco no final
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2] 
pessoa = fila.retira() #tiro o 3 do começo e nao coloco de volta, porque
                       #estamos matando de 3 em 3
[4, 5, 6, 7, 8, 9, 10, 1, 2] (só retira, mata o 3)
pessoa = fila.pop(0) #tiro o 4 do começo
fila.append(pessoa) #e coloco no final
[5, 6, 7, 8, 9, 10, 1, 2, 4] 
pessoa = fila.pop(0)
fila.append(pessoa)
[6, 7, 8, 9, 10, 1, 2, 4, 5]
pessoa = fila.retira()
[7, 8, 9, 10, 1, 2, 4, 5] (só retira, mata o 6)
[8, 9, 10, 1, 2, 4, 5, 7]
[9, 10, 1, 2, 4, 5, 7, 8]
[10, 1, 2, 4, 5, 7, 8]
[1, 2, 4, 5, 7, 8, 10]
[2, 4, 5, 7, 8, 10, 1]
[4, 5, 7, 8, 10, 1]
[5, 7, 8, 10, 1, 4]
[7, 8, 10, 1, 4, 5]
[8, 10, 1, 4, 5]
[10, 1, 4, 5, 8]
[1, 4, 5, 8, 10]
[4, 5, 8, 10]
[5, 8, 10, 4]
[8, 10, 4, 5]
[10, 4, 5]
[4, 5, 10]
[5, 10, 4]
[10, 4]
[4, 10]
[10, 4]
[4]
-> resposta: 4
'''



import unittest
import hashlib


class TestStringMethods(unittest.TestCase):

    def test_01_fila1(self):
        self.verifica_fila(fila1,'a6e09ce0ee14436cb70020b2fdbf640e79f88bfbc1d3b81276657a2d')
    
    def test_02_fila2(self):
        self.verifica_fila(fila2,'009f4fe1b80c470dec51da24864145a53a702b5263d09165e58475e1')
    
    def test_03_fila3(self):
        self.verifica_fila(fila3,'716dba572ee747af70f2fe863b1206c87244726185bb42a30fb5025c')

    def test_04_coloca_fila(self):
        fila = [1,2]
        coloca_fila(fila,5)
        self.assertEqual(fila,[1,2,5])
        coloca_fila(fila,10)
        self.assertEqual(fila,[1,2,5,10])
        fila = [1,2]
        coloca_fila(fila,10)
        self.assertEqual(fila,[1,2,10])

    def test_05_retira_fila(self):
        fila = [10,4,5]
        primeiro = retira(fila)
        self.assertEqual(primeiro,10)
        self.assertEqual(fila,[4,5])
        primeiro = retira(fila)
        self.assertEqual(primeiro,4)
        self.assertEqual(fila,[5])
        primeiro = retira(fila)
        self.assertEqual(primeiro,5)
        self.assertEqual(fila,[])
        fila = [11,12,13]
        primeiro = retira(fila)
        self.assertEqual(primeiro,11)
        self.assertEqual(fila,[12,13])

    def test_06_tamanho_fila(self):
        fila = [10,4,5]
        self.assertEqual(tamanho(fila),3)
        primeiro = retira(fila)
        self.assertEqual(tamanho(fila),2)
        primeiro = retira(fila)
        self.assertEqual(tamanho(fila),1)
        primeiro = retira(fila)
        self.assertEqual(tamanho(fila),0)


    def test_07_fila_vazia(self):
        fila = [4,50,2]
        self.assertFalse(fila_vazia(fila))
        primeiro = retira(fila)
        self.assertFalse(fila_vazia(fila))
        primeiro = retira(fila)
        self.assertFalse(fila_vazia(fila))
        primeiro = retira(fila)
        self.assertTrue(fila_vazia(fila))
        coloca_fila(fila,12)
        self.assertFalse(fila_vazia(fila))

    def test_08_primeiro(self):
        fila = [4,3,2]
        prim_num = primeiro(fila)
        self.assertEqual(prim_num,4)
        if fila != [4,3,2]:
            self.fail('nao era pra voce ter retirado nada da fila')

    def test_09_vira_1(self):
        soldados = [1,2,3,4]
        vira_1(soldados)
        self.assertEqual(soldados,[2,3,4,1])
        vira_1(soldados)
        self.assertEqual(soldados,[3,4,1,2])

    def test_10_vira_5(self):
        soldados = [1,2,3,4,5,6,7,8,9]
        vira_5(soldados)
        self.assertEqual(soldados,[6,7,8,9,1,2,3,4,5])
        vira_5(soldados)
        self.assertEqual(soldados,[2,3,4,5,6,7,8,9,1])

    def test_11_vira_n(self):
        soldados = [1,2,3,4,5,6,7,8,9]
        vira_n(soldados,5)
        self.assertEqual(soldados,[6,7,8,9,1,2,3,4,5])
        vira_n(soldados,5)
        self.assertEqual(soldados,[2,3,4,5,6,7,8,9,1])
        soldados = [1,2,3,4,5,6]
        vira_n(soldados,3)
        self.assertEqual(soldados,[4,5,6,1,2,3])
        vira_n(soldados,3)
        self.assertEqual(soldados,[1,2,3,4,5,6])
        vira_n(soldados,1)
        self.assertEqual(soldados,[2,3,4,5,6,1])
    def test_12_vira_4_mata_1(self):
        soldados = [1,2,3,4,5,6,7,8,9]
        vira_4_mata_1(soldados)
        self.assertEqual(soldados,[6,7,8,9,1,2,3,4])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados,[2,3,4,6,7,8,9])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados,[8,9,2,3,4,6])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados,[6,8,9,2,3])

    def test_13_fila_inicial(self):
        self.assertEqual(fila_inicial(4),[1,2,3,4])
        self.assertEqual(fila_inicial(8),[1,2,3,4,5,6,7,8])

    
    def test_20_josephus(self):
        self.assertEqual(josephus(5,2),3)
        self.assertEqual(josephus(6,3),1)
        self.assertEqual(josephus(1234,233),25)

    def verifica_fila(self,fila,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(fila).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
    
try:
    from josephus_gabarito import *
except:
    pass

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
