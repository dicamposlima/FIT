"""
O fatorial de 4 é 1*2*3*4
A definição é a mesma para qualquer inteiro:
fatorial de n = 1*2*3...*(n-1)*n
a unica excessao é o zero. Definimos fatorial de 0 como sendo 1

Quanto é fatorial de 0? de 1? de 6? Responda nas variaveis abaixo
"""

fatorial_6 = 720
fatorial_1 = 1
fatorial_0 = 1

"""
A variavel abaixo já vem preenchida com o fatorial de 100.

Preencha a variavel seguinte com o fatorial de 101
"""

fatorial_100 = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
fatorial_101 = 9425947759838359420851623124482936749562312794702543768327889353416977599316221476503087861591808346911623490003549599583369706302603264000000000000000000000000

"""
implemente uma funcao recursiva que calcula o fatorial

DICA: para passar nos primeiros testes, sua funcao
só tem que acertar o fatorial de 1 e de 0

Depois incremente ela para o resto usando recursao
"""


def fatorial(n):
    if n == 0:
        return 1
    return n*fatorial(n-1)


"""
    Uma definição simplista (e errada) de logaritmo:
log é o número de vezes que posso dividir um número por 2,
até obter 1 ou alguma coisa menor que 1
por exemplo, log(4)=2 (pois 4/2 dá 2, 2/2 dá 1)
outro exemplo, log(5)=3 (5/2 dá 2.5, 2.5/2 dá 1.25, 
1.25/2 dá menos do que 1)"""

"""
Qual é o log_tosco de 8? e 16? e 32? Responda nas variaveis abaixo
"""
log_8 = 3
log_16 = 4
log_32 = 5

"""
Sabendo que o log_tosco de 1000 é 10, quanto valem os logs
de 2000, 4000 e 8000 e 16000?
"""
log_2000 = 11
log_4000 = 12
log_8000 = 13
log_16000 = 14

"""
    Defina uma funcao log_tosco, recursiva, de acordo com
essa definição simplista de log

DICA: para passar no primeiro teste, voce só tem que 
acertar o log_tosco de 2. 

Depois melhore sua funcao, adicionando a recursao, para
resolver os outros casos e passar nos outros testes
"""


def log_tosco(n):
    if n <= 1:
        return 0
    return log_tosco(n/2)+1


"""
Explicacao
lembremos algumas coisas sobre listas.
Veja os exemplos a seguir

>>> lista
[564, 706, 153, 969, 490, 979, 924, 746, 879]
>>> lista[0] #significa primeiro elemento da lista, o de indice 0
564
>>> lista[1] #2o elemento, o de indice 1
706
>>> lista[3] #o primeiro tem indice 0. O segundo tem indice 1 ... o 4o tem indice 3
969
>>> lista[1:] #todos os elementos da lista a partir do elemento de indice 1
[706, 153, 969, 490, 979, 924, 746, 879]
>>> lista[3:] #todos os elementos da lista a partir do elemento de indice 3
[969, 490, 979, 924, 746, 879]

Quando escrevo lista[indice], pego o elemento da lista
que está na posicao dada pelo indice

Quando escrevo lista[indice:] pego o elemento
e todos os que vem depois dele

E o lista.pop(0)? 
o pop arranca elementos da lista.
fazer lista[1:] nao muda a lista, mas sim cria uma nova
"""

"""
defina uma funcao primeiro que recebe uma lista
e retorna o primeiro elemento dela
"""


def primeiro(lista):
    return lista[0]


"""
defina uma funcao todos_menos_primeiro que recebe
uma lista e retorna uma lista com todos os elementos
menos o primeiro.
"""


def todos_menos_primeiro(lista):
    return lista[1:]


"""
defina uma função recursiva maximo, que recebe uma lista
e retorna o maior de todos os números
que estão na lista

DICA: pra começar, faça a sua funcao funcionar para listas
com um unico elemento. Isso já passa o primeiro teste

Se o outro teste ficar complicado, tem mais uma dica embaixo
da funcao
"""


def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] if lista[0] > maximo(lista[1:]) else maximo(lista[1:])


"""
dica: uma coisa que você vai usar é o calculo recursivo do 
maximo de lista[1:]
ou seja, para resolver maximo([4,2,3]) voce vai pegar
lista[1:], que é [2,3], calcular recursivamente o máximo, que é 3,
e comparar com o lista[0], que é o 4, para achar o maior (no
caso, o maior entre 3 e 4 é 4)
"""

"""
Explicacao
>>> palavra='banana'
>>> palavra[0] #primeiro caractere, no indice 0
'b'
>>> palavra[2] #terceiro caractere, no indice 2
'n'
>>> palavra[2:] #a partir do indice 2
'nana'
>>> palavra[1:] #a partir do indice 1
'anana'

O mesmo acesso que vale para listas, também vale para
strings.
"""

"""
faça as funcoes primeira_letra e todas_as_letras_menos_primeira
"""


def primeira_letra(string):
    return string[0]


def todas_as_letras_menos_primeira(string):
    return string[1:]


"""
Defina uma função recursiva que recebe uma string e retorna
a string invertida

DICA: pra começar, faça sua função funcionar
para palavras com 0 ou 1 letra. Essas sao bem faceis de inverter :P
Só com isso você já passa um teste.

Se vc se complicar com a recursao, tem mais uma dica embaixo
da funcao
"""


def inverte(palavra):
    if len(palavra) < 2:
        return palavra
    return inverte(palavra[1:])+palavra[0]


"""    
dica: faça assim: pegue a primeira letra (palavra[0])
 e o resto (palavra[1:])
 inverta o resto depois junte palavra[0]
"""
"""
Retomando o log... quanto vale o log de um milhao?
Lembre-se que log_1000 = 10, e um milhao = 1000*1000
"""
log_1000000 = 20

"""
O próximo exercicio precisa de mais explicacao:

Imagine que estamos procurando um arquivo em
um computador.
Começamos pelo drive C, mas se nao achamos o arquivo,
devemos descer para as pastas presentes nele,
e tambem para as pastas presentes nas pastas.

Vamos implementar essa logica, procurando a string 'segredo'
em uma lista de listas. Ou seja: segredo pode estar
na lista principal, ou em uma lista dentro dela, ou em uma lista
dentro de uma lista dentro da lista principal (ou... bem, deve 
dar pra entender)

Rode os seguintes comandos no IDLE para entender o problema
Para gerar uma lista que contenha o segredo, use lista=gera(True)
Se ela não deve conter, use lista=gera(False)

Para imprimir uma lista, use imprime(lista)

Você deve implementar uma função recursiva que imprime True
se o segredo está na lista e False caso contrário

Pode gerar listas pra testar

Dica: implementei uma função eh_lista pra você usar.
eh_lista(variavel) retorna True se a variavel é uma lista,
False se nao é
"""



def acha_segredo(lista):
    if len(lista) == 0:
        return False
    if 'segredo' in lista:
        return True
    if eh_lista(lista[0]):
        return acha_segredo(lista[0]+lista[1:])
    return acha_segredo(lista[1:])

"""
Faça uma funcao conta_ll que recebe uma lista de listas e devolve
quantos numeros ela tem no total.

Por exemplo
conta_ll([]) retorna 0
conta_ll([[],[]]) retorna 0
conta_ll([[1,2],[3,4,2]]) retorna 5
observe, no exemplo acima temos uma lista com 2 listas dentro
[
[1,2],
[3,4,2]
]
conta_ll([[1,2],[3,4,2,[2]]]) retorna 6
observe, no exemplo acima temos uma lista com 2 listas dentro
e a segunda lista tem uma lista dentro
[
[1,2],
[3,4,2   , [2] ]
]
 conta_ll([1,2,[1,2],[3,4,2,[2]]]) retorna 8
observe, no exemplo acima temos uma lista com 2 numeros
e 2 listas dentro. A segunda lista tem uma lista dentro
[
1,
2,
[1,2],
[3,4,2   , [2] ]
]

Como você deve ter percebido pelo exemplo, uma lista
de listas pode conter varios niveis de listas, uma dentro da outra.

"""


def conta_ll(lista):
    if len(lista) == 0:
        return 0
    if eh_lista(lista[0]):
        return conta_ll(lista[0]+lista[1:])
    return (1 + conta_ll(lista[1:]))


"""
Implemente uma função anagramas 
que recebe uma palavra e devolve uma lista com todos 
os seus "embaralhamentos" (anagramas)

Por exemplo, anagramas('ab') deve retornar ['ab','ba']
Por exemplo, anagramas('abc') deve retornar ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""


def anagramas(palavra):
    if not palavra:
        return [palavra]
    anagrama = []
    subanagramas = anagramas(palavra[1:])
    for letra in subanagramas:
        for indice in range(len(letra) + 1):
            anagrama.append(letra[:indice] + palavra[0] + letra[indice:])
    return anagrama


"""
A partir daqui, não tem nada pra você implementar
"""

import random


def gera(coloca_segredo):
    return gera_r(2, 8, coloca_segredo)


def imprime(lista):
    pprint_list(lista)


def gera_r(max_subdirs, max_arquivos, coloca_segredo):
    subdirs, arquivos = 0, 0
    lista = []
    if (max_subdirs > 0):
        subdirs = random.randint(max_subdirs // 2, max_subdirs)
    for i in range(subdirs):
        lista2 = gera_r(max_subdirs - 1, max_arquivos - 1, False)
        lista.append(lista2)
    if (max_arquivos > 0):
        arquivos = random.randint(max_arquivos // 2, max_arquivos)
    for i in range(arquivos):
        lista.append(random.randint(0, arquivos))
    if (coloca_segredo):
        adiciona_segredo(lista)
    return lista


def adiciona_segredo(lista):
    plana = aplaina(lista)  # uma lista com todas as listas
    posicao = random.randint(0, len(plana) - 1)
    plana[posicao].append('segredo')


def aplaina(lista):
    plana = []
    plana.append(lista)
    for a in lista:
        if eh_lista(a):
            plana.extend(aplaina(a))
    return plana


def eh_lista(a):
    return isinstance(a, list)


def pprint_list(lista):
    pprint_list_r(lista, 0)


def pprint_list_r(lista, profund):
    arquivos = []
    sublistas = []
    espaco = '|    '
    for i in lista:
        if not eh_lista(i):
            arquivos.append(str(i))
        else:
            sublistas.append(i)
    print(espaco * profund + ', '.join(arquivos))
    for l in sublistas:
        print(espaco * profund + '/pasta:')
        pprint_list_r(l, profund + 1)
        print(espaco * profund + r'\ ')


import unittest
import sys
import hashlib


class TestStringMethods(unittest.TestCase):

    def test_001_variavel_fat6(self):
        self.valor_valido(fatorial_6, 'f10fcdd526499546551e174a5da16e9bc210909699d815b5d18b236f')

    def test_002_variavel_fat1(self):
        self.valor_valido(fatorial_1, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178')

    def test_003_variavel_fat0(self):
        self.valor_valido(fatorial_0, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178')

    def test_004_variavel_fat101(self):
        self.valor_valido(fatorial_101, 'fba13926f0f806fd20c8c39a3c77b39a791f6943a8afb4b9f625e6b9')

    def test_005_func_fatorial_acerta_um(self):
        self.assertEqual(fatorial(1), 1)

    def test_006_func_fatorial_acerta_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_007_fatorial_maiores(self):
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(5), 1 * 2 * 3 * 4 * 5)
        self.assertEqual(fatorial(10), 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)
        self.assertEqual(fatorial(50),
                         30414093201713378043612608166064768844377641568960512000000000000
                         )

    def test_008_fatorial_recursivo(self):
        sys.setrecursionlimit(50)
        # self.fail('a sua função é recursiva?')
        try:
            fatorial(60)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_100_var_log8(self):
        self.valor_valido(log_8, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474')

    def test_101_var_log16(self):
        self.valor_valido(log_16, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f')

    def test_102_var_log32(self):
        self.valor_valido(log_32, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17')

    def test_103_var_log2000(self):
        self.valor_valido(log_2000, '161a68601ec1d8ca45250557cff3ffb98eca53fbcf86bbdb8e8bb6e7')

    def test_103_var_log4000(self):
        self.valor_valido(log_4000, '3c794f0c67bd561ce841fc6a5999bf0df298a0f0ae3487efda9d0ef4')

    def test_103_var_log8000(self):
        self.valor_valido(log_8000, '86730f0dd6381286d3b5f0dfb897ce4895480ce97564c6be4f1543b8')

    def test_104_var_log16000(self):
        self.valor_valido(log_16000, 'e356f7a3e975871b64a30ec2390d130d5ff859054935857598fe3414')

    def test_105_log_tosco_de_dois(self):
        self.assertEqual(log_tosco(2), 1)

    def test_106_log_tosco_de_potencias_de_dois(self):
        self.assertEqual(log_tosco(2), 1)
        self.assertEqual(log_tosco(4), 2)
        self.assertEqual(log_tosco(8), 3)
        self.assertEqual(log_tosco(16), 4)
        self.assertEqual(log_tosco(128), 7)

    def test_108_log_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            log_tosco(2 ** 60)
            self.fail('a sua função log é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_200_primeiro(self):
        self.assertEqual(primeiro([1, 2, 3]), 1)
        self.assertEqual(primeiro([2, 3]), 2)
        self.assertEqual(primeiro([5]), 5)

    def test_201_todos_menos_primeiro(self):
        self.assertEqual(todos_menos_primeiro([1, 2, 3]), [2, 3])
        self.assertEqual(todos_menos_primeiro([2, 3]), [3])
        self.assertEqual(todos_menos_primeiro([5]), [])

    def test_202_max_lista_com_um_elemento(self):
        self.assertEqual(maximo([1]), 1)
        self.assertEqual(maximo([3]), 3)
        self.assertEqual(maximo([2]), 2)
        self.assertEqual(maximo([-1]), -1)

    def test_203_max(self):
        self.assertEqual(maximo([1, 2, 3]), 3)
        self.assertEqual(maximo([3, 2, 1]), 3)
        self.assertEqual(maximo([3, 10, 15, 30, 2, 1]), 30)

    def test_204_max_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            maximo(list(range(100)))
            self.fail('a sua função maximo é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao maximo é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_300_primeira_letra(self):
        self.assertEqual(primeira_letra('banana'), 'b')
        self.assertEqual(primeira_letra('abacaxi'), 'a')

    def test_301_todas_as_letras_menos_primeira(self):
        self.assertEqual(
            todas_as_letras_menos_primeira('banana'),
            'anana')
        self.assertEqual(
            todas_as_letras_menos_primeira('abacaxi'),
            'bacaxi')

    def test_302_inverte_pequeno(self):
        self.assertEqual(inverte('a'), 'a')
        self.assertEqual(inverte('b'), 'b')

    def test_303_inverte_vazia(self):
        self.assertEqual(inverte(''), '')

    def test_304_inverte(self):
        self.assertEqual(inverte('abb'), 'bba')
        self.assertEqual(inverte('ab'), 'ba')
        self.assertEqual(inverte('aba'), 'aba')

    def test_305_inverte_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            inverte('a' * 100)
            self.fail('a sua função inverte é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao inverte é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_700_o_retorno_do_log_tosco(self):
        self.assertEqual(log_tosco(1), 0)
        self.assertEqual(log_tosco(2), 1)
        self.assertEqual(log_tosco(5), 3)
        self.assertEqual(log_tosco(128), 7)
        self.assertEqual(log_tosco(1000), 10)

    def test_701_var_log1000000(self):
        self.valor_valido(log_1000000, '751267062c92e398c3942214b58136f73a4b9e1ca9a214d72d6d5805')

    def test_800_acha_segredo(self):
        for i in range(0, 100):
            if (i % 2 == 0):
                segredo = True
            else:
                segredo = False
            pasta = gera_r(4, 8, segredo)
            self.assertEqual(acha_segredo(pasta), segredo)

    def test_900_conta_ll(self):
        self.assertEqual(conta_ll([]), 0)
        self.assertEqual(conta_ll([[], []]), 0)
        self.assertEqual(conta_ll([[1, 2], [3, 4, 2]]), 5)
        self.assertEqual(conta_ll([[1, 2], [3, 4, 2, [2]]]), 6)
        self.assertEqual(conta_ll([1, 2, [1, 2], [3, 4, 2, [2]]]), 8)
        self.assertEqual(conta_ll([[[[[[[5]]]]]]]), 1)

    def test_901_anagramas(self):
        a = anagramas('abc')
        self.assertEqual(set(a), set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = anagramas('abcd')
        self.assertEqual(set(a), set(
            ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd',
             'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = anagramas('abca')
        self.assertEqual(set(a), set(
            ['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba',
             'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))

    def valor_valido(self, valor, codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(valor).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno, codigo_correto)


def codifica(valor):
    return hashlib.sha224(str(valor).encode('utf-8')).hexdigest()


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


runTests()
