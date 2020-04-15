import requests
import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_pessoas_retorna_lista(self):
        r = requests.get('http://localhost:5003/pessoas')
        self.assertEqual(type(r.json()),type([]))

    def test_001_adiciona_pessoas(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        #se ainda nao estiver funcionando, esse reseta acima, nao se preocupe
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'fernando','id':1})
        if r.status_code != 200:
            print('erro',r.json())
            self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'roberto','id':2})
        if r.status_code != 200:
            print('erro',r.json())
            self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5003/pessoas')
        achei_fernando = False
        achei_roberto = False
        for pessoa in r_lista.json():
            if pessoa['nome'] == 'fernando':
                achei_fernando = True
            if pessoa['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('pessoa fernando nao apareceu na lista de pessoas')
        if not achei_roberto:
            self.fail('pessoa roberto nao apareceu na lista de pessoas')

    def test_002_pessoa_por_id(self):
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'mario','id':20})
        r_lista = requests.get('http://localhost:5003/pessoas/20')
        self.assertEqual(r_lista.json()['nome'],'mario')


    
    def test_003_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'cicero','id':29})
        r_lista = requests.get('http://localhost:5003/pessoas')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5003/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5003/pessoas')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_100_interesse_com_pessoas_validas(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'maximus','id':9})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,404)
        r = requests.put('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,404)
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'aurelia','id':3})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,200)


    def test_101_match(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,404)
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'maximus','id':9})
        self.assertEqual(r.status_code,200)

        #maximus acabou de ser criado, nao tem matches
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])
        
        #crio aurelia
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'aurelia','id':3})
        self.assertEqual(r.status_code,200)
        
        #maximus está interessado em aurélia, mas ainda não é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

        #agora é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[3])

        #crio diana
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'diana','id':30})
        self.assertEqual(r.status_code,200)
        
        #maximus está interessado em diana, mas ainda não é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/30/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[3])

        #agora é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/30/9/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        lista_de_matches = r.json()
        self.assertIn(3,lista_de_matches)
        self.assertIn(30,lista_de_matches)

        #aurélia também tem o match
        r = requests.get('http://localhost:5003/matches/3')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[9])

        #e igualmente diana
        r = requests.get('http://localhost:5003/matches/30')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[9])


    def test_102_match_perdido(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,404)
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'maximus','id':9})
        self.assertEqual(r.status_code,200)

        #maximus acabou de ser criado, nao tem matches
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])
        
        #crio aurelia
        r = requests.post('http://localhost:5003/pessoas',json={'nome':'aurelia','id':3})
        self.assertEqual(r.status_code,200)
        
        #maximus está interessado em aurélia, mas ainda não é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

        #agora é reciproco
        r = requests.put('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[3])

        #aurélia perde o interesse
        r = requests.delete('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

    def test_103_match_incompativel(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,404)
        maximus = {'nome':'maximus','id':9,'sexo':'homem','buscando':['mulher']}
        r = requests.post('http://localhost:5003/pessoas',json=maximus)
        self.assertEqual(r.status_code,200)

        #maximus acabou de ser criado, nao tem matches
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])
        
        #crio aurelia
        aurelia = {'nome':'aurelia','id':3,'sexo':'mulher','buscando':['mulher']}
        r = requests.post('http://localhost:5003/pessoas',json=aurelia)
        self.assertEqual(r.status_code,200)

        #maximus está interessado em aurélia
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

        #aurelia manifesta interesse em maximus, de forma incompativel
        #com suas preferências anteriores
        r = requests.put('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['erro'],'interesse incompativel')
        #esse erro ocorre quando A manifesta interesse em M, 
        #mas A declarou anteriormente que nao tem interesse 
        #em ninguém do sexo de M
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

    def test_104_match_compativel(self):
        r_reset = requests.post('http://localhost:5003/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,404)
        maximus = {'nome':'maximus','id':9,'sexo':'homem','buscando':['homem','mulher']}
        r = requests.post('http://localhost:5003/pessoas',json=maximus)
        self.assertEqual(r.status_code,200)

        #maximus acabou de ser criado, nao tem matches
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])
        
        #crio aurelia
        aurelia = {'nome':'aurelia','id':3,'sexo':'mulher','buscando':['mulher','homem']}
        r = requests.post('http://localhost:5003/pessoas',json=aurelia)
        self.assertEqual(r.status_code,200)

        #maximus está interessado em aurélia
        r = requests.put('http://localhost:5003/sinalizar_interesse/9/3/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[])

        #aurelia manifesta interesse em maximus
        r = requests.put('http://localhost:5003/sinalizar_interesse/3/9/')
        self.assertEqual(r.status_code,200)
        r = requests.get('http://localhost:5003/matches/9')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json(),[3])


        





    

    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
