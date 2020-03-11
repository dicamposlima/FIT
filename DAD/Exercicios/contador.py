import unittest
class TestStringMethods(unittest.TestCase):

     def test_01_contador_retorna_dic(self):
         texto=('o doce mais doce').split()
         d = {}
         for lista in texto:          
            d[lista]=1
         self.assertEqual(type(d),type({'dicionario':'exemplo'}))

     def test_02_contador(self):
        texto=('esse exercício é um exercício fácil ou difícil').split()
        d2 = {}
        for lista in texto:
          if lista in d2:
            d2[lista] = d2[lista]+1
          else:
            d2[lista]=1
 	
        self.assertEqual(d2,{'é': 1, 'difícil': 1,
                            'esse': 1, 'ou': 1, 'um': 1, 'fácil': 1, 'exercício': 2})

        texto=('o doce perguntou ao doce qual é o doce mais doce '+
                    'e o doce respondeu ao doce que o doce mais doce é '+
                    'o doce de batata doce').split()
        d3 = {}
        for lista in texto:
          if lista in d3:
            d3[lista] = d3[lista]+1
          else:
            d3[lista]=1
        self.assertEqual(d3['doce'],10)
        self.assertTrue('gato' not in d3)
        self.assertTrue('respondeu' in d3)
     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
    from gabarito_contador import *
    runTests()
except:
    pass
