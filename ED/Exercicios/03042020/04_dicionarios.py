import unittest

#faça uma funcao que conta as letras de uma string
#por exemplo, 'banana' tem 3 letras 'a'
# a funcao recebe uma string e devolve um dicionário
# por exemplo, conta_letras('banana') devolve {'b':1,'a':3,'n':2}
def conta_letras(string):
    dicti = {}
    for letra in string:
        if letra not in dicti:
            dicti[letra] = 1
        else:
            dicti[letra] = dicti[letra]+1
    return dicti



#faça uma funcao que decide se duas funções sao "embaralhamentos"
#uma da outra. 
#por exemplo, 'banana' e 'nabana' tem as mesmas letras, so muda
# a ordem. Dizemos que sao anagramas.
# note que a quantidade de cada letra importa: 'abb' e 'aab' 
# nao sao anagramas.
# a funcao deve recber duas strings e retornar True se elas sao
# anagramas, False caso contrário
# DICA: voce pode usar sua funcao de contar letras
def anagrama(string1,string2):
    return conta_letras(string1) == conta_letras(string2)

'''
Faça uma função que recebe uma palavra e diz qual a letra 
mais frequente.
Não se preocupe com empates nem com  a string vazia
'''
def letra_mais_freq(palavra):
    dicti = conta_letras(palavra)
    for key, value in dicti.items():
        if value == max(dicti.values()):
            return key
    return 0
      



class TestPartThree(unittest.TestCase):
    def test_13_conta_letras(self):
        testes = [('banana',{'b':1,'a':3,'n':2}),
                  ('nabana',{'b':1,'a':3,'n':2}),
                  ('abb',{'b':2,'a':1}),
                  ('baa',{'b':1,'a':2}),
                  ('',{})
                  ]
        for teste in testes:
             self.assertEqual(conta_letras(teste[0]),
                                   teste[1])

    
    def test_14_verifica_anagrama(self):
        self.assertEqual(anagrama('banana','nabana'),True)
        self.assertEqual(anagrama('banaaa','nabana'),False)
        self.assertEqual(anagrama('banana','nabann'),False)
        self.assertEqual(anagrama('abb','bba'),True)
        self.assertEqual(anagrama('abb','aab'),False)
        self.assertEqual(anagrama('abab','baba'),True)
        self.assertEqual(anagrama('',''),True)
        self.assertEqual(anagrama('','a'),False)
        self.assertEqual(anagrama('a',''),False)
    
    def test_15_letra_mais_freq(self):
        self.assertEqual(letra_mais_freq('banana'),'a')
        self.assertEqual(letra_mais_freq('aaab'),'a')
        self.assertEqual(letra_mais_freq('bbbbba'),'b')
        self.assertEqual(letra_mais_freq('c'),'c')

        



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartThree)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()