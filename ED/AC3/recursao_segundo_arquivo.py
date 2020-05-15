def soma_n_primeiros(n: int) -> int:
    """
    função recursiva soma_n_primeiros.

    Ela recebe um número e retorna a soma de todos os numeros inteiros até ele

    por exemplo, soma_n_primeiros(3) retorna 6 (que é 1+2+3)
    por exemplo, soma_n_primeiros(5) retorna 15 (que é 1+2+3+4+5)
    por exemplo, soma_n_primeiros(100) retorna 5050 (que é 1+2+3+4+5...+99+100)
    por exemplo, soma_n_primeiros(1) retorna 1
    :param n: int
    :return: int
    """
    return 1 if n == 1 else n + soma_n_primeiros(n - 1)


def soma_lista(lista: list) -> int:
    """
    função recursiva soma_lista
    que recebe uma lista e retorna a soma
    de todos os seus elementos

    por exemplo, soma_lista([10,2]) retorna 12
    por exemplo, soma_lista([10,2,3]) retorna 15
    :param lista: list
    :return: int
    """
    return 0 if len(lista) == 0 else lista[0] + soma_lista(lista[1:])


def conta_recursiva(lista: list, numero: int) -> int:
    """
    função recursiva conta_recursiva, que
    recebe uma lista e um numero, e diz quantas vezes o número
    aparece na lista.

    Por exemplo conta_recursiva([0,1,2,1,4],1) retorna 2
    Por exemplo conta_recursiva([0,1,2,1,4],4) retorna 1
    Por exemplo conta_recursiva([0,1,2,1,4],5) retorna 0
    Por exemplo conta_recursiva([],5) retorna 0
    :param lista: list
    :param numero: int
    :return: int
    """
    if len(lista) == 0:
        return 0
    return conta_recursiva(lista[1:], numero) + 1 \
        if lista[0] == numero else conta_recursiva(lista[1:], numero)


def filtro_recursivo(lista, numero: int):
    """
    função recursiva filtro_recursivo
    ela recebe uma lista e um numero e retorna a lista,
    tirando todas as vezes que o número aparece

    Por exemplo filtro_recursivo([0,1,2,1,4],1) retorna [0,2,4]
    Por exemplo filtro_recursivo([0,1,2,1,4],4) retorna [0,1,2,1]
    Por exemplo filtro_recursivo([0,1,2,1,4],5) retorna [0,1,2,1,4]
    Por exemplo filtro_recursivo([],5) retorna []
    :param lista: list|int
    :param numero: int
    :return: list|int
    """
    if len(lista) == 0:
        return []
    return filtro_recursivo(lista[1:], numero) \
        if lista[0] == numero else [lista[0]] + filtro_recursivo(lista[1:], numero)


def palindromo_recursivo(string: str) -> bool:
    """
    função recursiva palindromo_recursivo,
    que recebe uma string e retorna
    True se ela é um palindromo, False caso contrario.

    Um palindromo é uma string "espelhada"

    Por exemplo palindromo_recursivo('abbabba') retorna True
    Por exemplo palindromo_recursivo('aaa') retorna True
    Por exemplo palindromo_recursivo('aaaa') retorna True
    Por exemplo palindromo_recursivo('aac') retorna False
    Por exemplo palindromo_recursivo('a') retorna True
    Por exemplo palindromo_recursivo('') retorna True

    dicas:
        string[0] é o primeiro elemento
        string[-1] é o ultimo
        string[1:-1] é a string sem o primeiro nem o ultimo
        (teste no terminal do python!)
    :param string: str
    :return: bool
    """
    if len(string) == 0:
        return True
    return palindromo_recursivo(string[1:-1]) if string[0] == string[-1] else False


def troca_recursiva(lista: list, tirar: int, colocar: int) -> list:
    """
    função recursiva troca_recursiva
    ela recebe uma lista e dois numeros (tirar e colocar)
    e retorna a lista, trocando o numero tirar pelo colocar

    Por exemplo troca_recursiva([0,1,2,1,4],1,5) retorna [0,5,2,5,4]
    Por exemplo troca_recursiva([0,1,2,1,4],4,7) retorna [0,1,2,1,7]
    Por exemplo troca_recursiva([0,1,2,1,4],5,6) retorna [0,1,2,1,4]
    Por exemplo troca_recursiva([],5) retorna []
    :param lista: list
    :param tirar: int
    :param colocar: int
    :return: list
    """
    if len(lista) == 0:
        return []
    return [colocar] + troca_recursiva(lista[1:], tirar, colocar) \
        if lista[0] == tirar else [lista[0]] + troca_recursiva(lista[1:], tirar, colocar)


def eh_lista(a: list) -> bool:
    """
    retorna True se um objeto é lista e False se não é
    :param a: list
    :return: bool
    """
    return isinstance(a, list)


def soma_ll(lista: list) -> int:
    """
    funcao soma para listas de listas

    Por exemplo, considere a lista [[[1,2,3],[4,5],11,4],9,8,4]

    O seu primeiro elemento é uma lista
    [[1,2,3],[4,5],11,4]

    Essa lista tem o primeiro elemento sendo uma lista: [1,2,3]
    e o segundo também: [4,5]

    Ou seja, uma lista de listas pode conter listas que também contem listas:
    [[[[[1]]],2]] é uma lista de listas válida

    Por exemplo, soma_ll([[[1,2,3],[4,5],11,4],9,8,4]) é 46
    :param lista: list
    :return: int
    """
    if len(lista) == 0:
        return 0
    return soma_ll(lista[0] + lista[1:]) \
        if eh_lista(lista[0]) else lista[0] + soma_ll(lista[1:])


def anagramas(palavra: str) -> list:
    """
    função anagramas
    que recebe uma palavra e devolve uma lista com todos
    os seus "embaralhamentos" (anagramas)

    Por exemplo, anagramas('ab') deve retornar ['ab','ba']
    :param palavra: str
    :return: list
    """
    if palavra:
        anagrama = []
        subanagramas = anagramas(palavra[1:])
        for letra in subanagramas:
            for indice in range(len(letra) + 1):
                anagrama.append(letra[:indice] + palavra[0] + letra[indice:])
        return anagrama
    else:
        return ['']



'''
A partir daqui, não tem nada pra você implementar
'''

import sys
import unittest


class TestStringMethods(unittest.TestCase):

    def test_000_soma_n_primeiros_caso_facil(self):
        self.assertEqual(soma_n_primeiros(1), 1)

    def test_001_soma_n_primeiros_funciona(self):
        self.assertEqual(soma_n_primeiros(3), 6)
        self.assertEqual(soma_n_primeiros(5), 15)
        self.assertEqual(soma_n_primeiros(100), 5050)
        self.assertEqual(soma_n_primeiros(10), 55)

    def test_002_soma_n_primeiros_eh_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            a = soma_n_primeiros(1000)
            print(a)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_100_soma_lista_casos_faceis(self):
        self.assertEqual(soma_lista([1]), 1)
        self.assertEqual(soma_lista([]), 0)
        self.assertEqual(soma_lista([-3]), -3)

    def test_101_soma_lista_funciona(self):
        self.assertEqual(soma_lista([1, 2, 30]), 33)
        self.assertEqual(soma_lista([1, 3, 5]), 9)
        self.assertEqual(soma_lista([10, 2, 3, 4]), 19)
        self.assertEqual(soma_lista([-1, -2, -3, -4]), -10)

    def test_102_soma_lista_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            soma_lista([1] * 100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_200_conta_caso_facil(self):
        self.assertEqual(conta_recursiva([], 5), 0)
        self.assertEqual(conta_recursiva([5], 5), 1)
        self.assertEqual(conta_recursiva([1], 5), 0)

    def test_201_conta_pequena(self):
        self.assertEqual(conta_recursiva([0, 1, 2, 1, 4], 1), 2)
        self.assertEqual(conta_recursiva([0, 1, 2, 1, 4], 4), 1)
        self.assertEqual(conta_recursiva([1, 1], 1), 2)
        self.assertEqual(conta_recursiva([1, 1], 2), 0)
        self.assertEqual(conta_recursiva([0, 1, 2, 1, 4], 5), 0)

    def test_202_conta_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            conta_recursiva([1] * 100, 1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_301_filtro_caso_facil(self):
        self.assertEqual(filtro_recursivo([], 5), [])
        self.assertEqual(filtro_recursivo([1], 5), [1])

    def test_302_filtro_funciona(self):
        self.assertEqual(filtro_recursivo([0, 1, 2, 1, 4], 1), [0, 2, 4])
        self.assertEqual(filtro_recursivo([0, 1, 2, 1, 4], 4), [0, 1, 2, 1])
        self.assertEqual(filtro_recursivo([1, 1], 1), [])
        self.assertEqual(filtro_recursivo([1, 1], 2), [1, 1])
        self.assertEqual(filtro_recursivo([0, 1, 2, 1, 4], 5), [0, 1, 2, 1, 4])

    def test_303_filtro_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            filtro_recursivo([1] * 100, 1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_400_palindromo_caso_facil(self):
        self.assertEqual(palindromo_recursivo('a'), True)
        self.assertEqual(palindromo_recursivo(''), True)

    def test_401_palindromo_funciona(self):
        self.assertEqual(palindromo_recursivo('abbabba'), True)
        self.assertEqual(palindromo_recursivo('aaa'), True)
        self.assertEqual(palindromo_recursivo('aaaa'), True)
        self.assertEqual(palindromo_recursivo('aac'), False)

    def test_402_palindromo_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            palindromo_recursivo('a' * 100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_500_troca_caso_facil(self):
        self.assertEqual(troca_recursiva([], 5, 2), [])
        self.assertEqual(troca_recursiva([1], 5, 4), [1])
        self.assertEqual(troca_recursiva([5], 5, 4), [4])

    def test_501_troca_funciona(self):
        self.assertEqual(troca_recursiva([0, 1, 2, 1, 4], 1, 7), [0, 7, 2, 7, 4])
        self.assertEqual(troca_recursiva([0, 1, 2, 1, 4], 4, 9), [0, 1, 2, 1, 9])
        self.assertEqual(troca_recursiva([1, 1], 1, 2), [2, 2])
        self.assertEqual(troca_recursiva([1, 1], 2, 7), [1, 1])
        self.assertEqual(troca_recursiva([0, 1, 2, 1, 4], 5, 3), [0, 1, 2, 1, 4])
        self.assertEqual(troca_recursiva([0, 1, 2, 1, 4], 0, 0), [0, 1, 2, 1, 4])
        self.assertEqual(troca_recursiva([0, 1, 2, 1, 4], 9, 9), [0, 1, 2, 1, 4])

    def test_502_troca_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            troca_recursiva([1] * 100, 1, 2)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_600_soma_ll(self):
        self.assertEqual(soma_ll([1, 2, 3]), 6)
        self.assertEqual(soma_ll([1, 2, 3, 4]), 10)
        self.assertEqual(soma_ll([-1, -2, -3, -4]), -10)
        self.assertEqual(soma_ll([1]), 1)
        self.assertEqual(soma_ll([]), 0)
        self.assertEqual(soma_ll([-3]), -3)
        self.assertEqual(soma_ll([[], []]), 0)
        self.assertEqual(soma_ll([[1], [2]]), 3)
        self.assertEqual(soma_ll([[[1, 2, 3], [4, 5], 11], 9, 8]), 43)
        self.assertEqual(soma_ll([[[1, 2, 3], [4, 5], 11, 4], 9, 8, 4]), 51)
        self.assertEqual(soma_ll([[-1], [1]]), 0)
        self.assertEqual(soma_ll([[1], [[2], 1]]), 4)

    def test_700_anagramas(self):
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


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


try:
    from recursao_segundo_arquivo_respostas import *
except:
    pass

runTests()
