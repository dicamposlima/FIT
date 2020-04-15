
'''
faça uma função que recebe uma lista de números e retorna a
soma de todos eles. NÃO utilize a função sum do python. Implemente a
lógica você mesmo!
'''
def soma(lista):
    soma = 0
    for element in lista:
        soma += element
    return soma

#faça uma função que recebe uma lista de números e retorna a média.
#ou seja, soma todos os números e divide pela quantidade de numeros
def media(lista):
    return (soma(lista)/len(lista))

#faça uma função que acrescenta o proximo numero a uma lista.
#por exemplo cresce([7,8]) deve devolver [7,8,9]
def cresce(lista):
    lista.append(lista[-1]+1)
    return lista

'''
Explicacao

As próximas duas funções tem a ver com baralho.

A idéia é representar cada carta como uma string de 2 letras:
    as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
    os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
    
O J de ouros, por exemplo, é representado pela string 'Jo'. O ás de copas,
pela string 'Ac'
'''

'''
faça uma função que recebe um naipe de cartas ('o', que significa ouros,
'p', que significa paus, 'c' de copas ou 'e' de espadas) e retorna 
uma lista com todas as cartas desse naipe.

Entao, se você receber 'c', deve retornar deve retornar uma lista com 13 cartas, 
o ás de copas representado pela string 'Ac', os números '2c','3c',...'10c'
e as figuras,  'Jc', 'Qc', 'Kc'.

Dica: para juntar duas strings, faça nova='a'+'b'
Dica: para transformar um numero n em string, faça str(n)
'''
def cria_naipe(naipe):
    return [element + naipe for element in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]
    # return f"{naipe} ".join(map(str, ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",""])).split(" ")[0:13]
    # return [element + naipe for element in ['A',*['A',*[str(numeros) for numeros in range(2,11)],'J','Q','K'],'J','Q','K']]


#faça uma função que cria um baralho completo, com todas as 52 cartas
#ela nao recebe nada e retorna uma lista.
#os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
#as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
#O J de ouros, por exemplo, é representado pela string 'Jo'. 
#Assim 'Jo' é um dos elementos que deve aparecer na lista
def cria_baralho():
    return cria_naipe('o')+cria_naipe('c')+cria_naipe('e')+cria_naipe('p')

#Faça uma função que recebe uma lista, 
#e retorna todos os valores dessa lista que estao acima da média.
# Por exemplo, considerando [1,2,3,4,5], temos média 3. 
# Assim acima_da_media([1,2,3,4,5]) deve retornar a lista [4,5]
# Voce pode usar a sua funçao de média, que implementou antes
def acima_da_media(lista):
    medval = media(lista)
    acima = []
    for element in lista:
        if element > medval:
            acima.append(element)
    return acima

# Uma loja está fazendo uma liquidaçao.
# A funçao liquidacao receberá duas listas. 
# Uma contém preços (em reais) e a outra descontos (tb em reais)
# Retorne uma terceira lista, dos preços já com desconto.
# Assim, por exemplo, liquidacao([2,4],[0,3]) 
# é uma situação em que o produto de preço 2 tem 0 reais de desconto 
# e o produto de preço 4 tem 3 reais de desconto
# A função deve retornar a lista [2,1]
def  liquidacao(precos,descontos):
    tamano = min(len(precos),len(descontos))
    return [precos[i]-descontos[i] for i in range(tamano)]


import unittest

class TestPartTwo(unittest.TestCase):
    

    def test_04_sum_simple(self):
        self.assertEqual(soma([1,2,3]), 6)
        self.assertEqual(soma([3,2,1]), 6)
        self.assertEqual(soma([3,10,15,30,2,1]), 61)
    
    def test_05_sum_small(self):
        self.assertEqual(soma([-1]), -1)
        self.assertEqual(soma([3]), 3)
        self.assertEqual(soma([]), 0)

    def test_08_media(self):
        self.assertEqual(media([1]),
                         1)
        self.assertEqual(media([1,2]),
                         1.5)
        self.assertEqual(media([1,2,3]),
                         2)

    def test_09_cresce(self):
        self.assertEqual(cresce([1]),
                         [1,2])
        self.assertEqual(cresce([5]),
                         [5,6])
        self.assertEqual(cresce([5,6]),
                         [5,6,7])
        self.assertEqual(cresce([5,6,7,8,9]),
                         [5,6,7,8,9,10])

    def test_10_cria_naipe(self):
        copas_correto = set(['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc'])
        copas_gerado = set(cria_naipe('c'))
        self.assertEqual(copas_gerado,copas_correto)
        paus_correto = set(['Ap', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', 'Jp', 'Qp', 'Kp'])
        paus_gerado = set(cria_naipe('p'))
        self.assertEqual(paus_gerado,paus_correto)
    
    def test_11_cria_baralho(self):
        baralho_correto = set(['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ae', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', '10e', 'Je', 'Qe', 'Ke', 'Ao', '2o', '3o', '4o', '5o', '6o', '7o', '8o', '9o', '10o', 'Jo', 'Qo', 'Ko', 'Ap', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', 'Jp', 'Qp', 'Kp'])
        baralho_gerado = set(cria_baralho())
        self.assertEqual(baralho_gerado,baralho_correto)

    def test_12_acima_da_media(self):
        self.assertEqual(set(acima_da_media([1,2,3])),{3})
        conj_vazio = set()
        self.assertEqual(set(acima_da_media([2,2,2])),conj_vazio)
        self.assertEqual(set(acima_da_media([-2,0,1])),{0,1})

       
    def test_13_liquidacao(self):
        precos=[10,10,10],[0],[10,20,30],[1,2,3,4]
        descontos=[1,1,1],[0],[9,8,7],[1,1,1,1]
        final=[9,9,9],[0],[1,12,23],[0,1,2,3]
        for i in range(0,len(precos)):
            self.assertEqual(liquidacao(precos[i],descontos[i])
                                ,final[i])






def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartTwo)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)
"""
try:
    from listas_gabarito import *
    runTests();
except:
    pass
"""
if __name__ == '__main__':
    runTests()