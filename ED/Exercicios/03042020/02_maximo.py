
'''
defina uma funcao maximo2 que recebe dois numeros e retorna o maior deles
'''
def maximo2(a,b):
    return a if a > b else b

'''
defina uma funcao maximo3 que recebe três numeros e retorna o maior deles
'''
def maximo3(a,b,c):
    maior = maximo2(a, b)
    return maximo2(maior, c)

'''
defina uma funcao maximo4 que recebe quatro numeros e retorna o maior deles
'''
def maximo4(a,b,c,d):
    maior = maximo3(a, b, c)
    return maximo2(maior, d)

'''
defina uma funcao maximo5 que recebe cinco numeros e retorna o maior deles
'''
def maximo5(a,b,c,d,e):
    maior = maximo4(a, b, c, d)
    return maximo2(maior, e)

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_maximo2(self):
        self.assertEqual(maximo2(1,2),2)
        self.assertEqual(maximo2(3,2),3)
        self.assertEqual(maximo2(-1,-2),-1)
        self.assertEqual(maximo2(-1,2),2)
    
    def test_maximo3(self):
        self.assertEqual(maximo3(1,2,3),3)
        self.assertEqual(maximo3(10,2,3),10)
        self.assertEqual(maximo3(1,20,3),20)
    
    def test_maximo4(self):
        self.assertEqual(maximo4(1,2,3,4),4)
        self.assertEqual(maximo4(10,2,3,4),10)
        self.assertEqual(maximo4(1,20,3,4),20)
        self.assertEqual(maximo4(1,2,30,4),30)
    
    def test_maximo5(self):
        self.assertEqual(maximo5(10,2,3,4,5),10)
        self.assertEqual(maximo5(1,20,3,4,5),20)
        self.assertEqual(maximo5(1,2,30,4,5),30)
        self.assertEqual(maximo5(1,2,3,40,5),40)
        self.assertEqual(maximo5(1,2,3,4,50),50)

    

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()