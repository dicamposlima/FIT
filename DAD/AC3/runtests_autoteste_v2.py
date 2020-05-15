import requests
import unittest

url = 'http://localhost:5004/autoteste/'

class TestStringMethods(unittest.TestCase):


    '''
    se eu acessar a url /autoteste/questoes, gostaria de receber
    uma lista com pelo menos 2 questões
    '''
    def test_001_todas_questoes(self):
        r = requests.get(url+'questoes')
        self.assertEqual(type(r.json()),type([]))
        self.assertTrue(len(r.json())>=2)
    
    '''
    essa funcao não é um teste, mas auxilia os testes
    ela verifica, na lista de questoes, se alguma tem 
    o texto passado
    '''
    def verifica_questao(self,texto_questao):
        r = requests.get(url+'questoes')
        lista_questoes = r.json()
        for dic_questao in lista_questoes:
            if dic_questao['pergunta'] == texto_questao:
                return True
        return False

    '''
    Verifica se algumas questoes aparecem na lista do servidor
    '''
    def test_001a_questoes_presentes(self):
        self.assertTrue(self.verifica_questao('O que quer dizer RPC?'))
        self.assertFalse(self.verifica_questao('Is this the real life?'))
        self.assertFalse(self.verifica_questao('Or is it just fantasy?'))
        self.assertTrue(self.verifica_questao('Quanto vale 2**6?'))

    '''
    Verifica se é possivel baixar o dicionario de respostas
    do servidor, acessando a url /autoteste/respostas com o verbo GET
    '''
    def test_002_respostas(self):
        r = requests.get(url+'respostas')
        self.assertEqual(type(r.json()),type({}))
        self.assertTrue(len(r.json())>=2)
   
    '''
    Ao baixar o dicionário de respostas, verifica se as pessoas
    certas aparecem
    '''
    def test_002a_respondedores_presentes(self):
        r = requests.get(url+'respostas')
        dic_devolvido = r.json()
        self.assertTrue('marcio' in dic_devolvido)
        self.assertFalse('bonde' in dic_devolvido)
    '''
    ao acessar a url /autoteste/questao/1, devemos
    receber o dicionário da questão 1
    '''
    def test_003_busca_questao_por_id(self):
        r = requests.post(url+'reseta')
        r = requests.get(url+'questao/1')
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],1)
        self.assertEqual(dic_retornado['corretas'],['Remote procedure call'])
        r = requests.get(url+'questao/2')
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],2)
        self.assertIn(12,dic_retornado['erradas'])

    '''
    Ao fazer usar o verbo post na url /autoteste/questao,
    podemos enviar um dicionário e criar uma nova questão
    '''
    def test_004_cria_questao(self):
        q1 = {
            'pergunta': 'Quanto vale 3+4?',
            'erradas': [12,36,26,32],
            'corretas': [7]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        #o texto da minha pergunta é q1['pergunta']
        #baixo a lista e verifico se esse texto aparece nela
        self.assertTrue(self.verifica_questao(q1['pergunta']))
    
    '''
    Fazemos o mesmo teste anterior, mas queremos conferir o id da questão
    '''
    def test_004a_cria_questao_ids_ok(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Quanto vale 3+4?',
            'erradas': [12,36,26,32],
            'corretas': [7]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        #baixo a questao 3 e verifico deu certo
        r = requests.get(url+'questao/3')
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],3)
        self.assertEqual(dic_retornado['corretas'],[7])

    '''
    A url de reseta já deveria estar ok.
    Esse teste é de graça se você não bagunçar isso :P
    '''
    def test_005_reset(self):
        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        self.assertTrue(self.verifica_questao(q1['pergunta']))
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        self.assertFalse(self.verifica_questao(q1['pergunta']))
        self.assertTrue(self.verifica_questao('O que quer dizer RPC?'))
        self.assertTrue(self.verifica_questao('Quanto vale 2**6?'))
        
        r = requests.get(url+'questoes')
        self.assertEqual(len(r.json()),2)

    '''
    Tento acessar uma questão que não existe.
    Espero um erro 404
    '''
    def test_006_busca_questao_por_id_404(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'questao/1')
        self.assertEqual(r.status_code,200)
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],1)
        self.assertEqual(dic_retornado['corretas'],['Remote procedure call'])
        r = requests.get(url+'questao/10')
        self.assertEqual(r.status_code,404)
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['erro'],'Questao nao encontrada')
   
    '''
    Tento criar uma questao incompleta e vejo se dá erro
    '''
    def test_007_tentar_criar_questao_com_dic_incompleto(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }

        
        #criar uma questao sem a chave pergunta deve dar erro
        q_copy = q1.copy()
        del q_copy['pergunta']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)


        #criar uma questao sem a chave erradas deve dar erro
        q_copy = q1.copy()
        del q_copy['erradas']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)


        #criar uma questao sem a chave corretas deve dar erro
        q_copy = q1.copy()
        del q_copy['corretas']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)

        #criar uma questao sem deletar nenhuma chave deve funcionar
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
    
    '''
    usando put na url /autoteste/questao/1/erradas,
    adiciono alternativas erradas para questao 1
    '''
    def test_008a_adiciona_alternativas_erradas_em_uma_questao(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
      
        #monto o dicionario das erradas pra fazer o envio
        erradas = {}
        erradas['erradas'] = ['roberto pula o caminhao']
        #ele tem a chave erradas,que é uma lista com as alternativas
        #erradas a adicionar

        r = requests.put(url+'questao/1/erradas', json = erradas)
        self.assertEqual(r.status_code,200)
        
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['erradas']),3)
        self.assertEqual(devolvida['erradas'][-1],'roberto pula o caminhao')

    
    def test_008b_adiciona_alternativas_erradas_repetidas(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
      
        #monto o dicionario das erradas pra fazer o envio
        erradas = {}
        erradas['erradas'] = ['roberto pula o caminhao']
        #ele tem a chave erradas,que é uma lista com as alternativas
        #erradas a adicionar

        r = requests.put(url+'questao/1/erradas', json = erradas)
        self.assertEqual(r.status_code,200)
        
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['erradas']),3)
        self.assertEqual(devolvida['erradas'][-1],'roberto pula o caminhao')

        #tento colocar de novo...
        r = requests.put(url+'questao/1/erradas', json = erradas)
        
        #...mas isso muda nada. A lista de erradas tinha 3
        #elementos, e continua tendo 3 elementos
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['erradas']),3)
    
    #tento adicionar alternativas em uma questao que nao existe
    def test_008c_adiciona_alternativas_erradas_404(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        erradas = {}
        erradas['erradas'] = ['roberto pula o caminhao']

        #se tento adicionar em uma questao que nao existe
        r = requests.put(url+'questao/3/erradas', json = erradas)
        #devo ter um cod de status 404
        self.assertEqual(r.status_code,404)
    
    def test_009a_adiciona_alternativas_corretas_em_uma_questao(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        #monto o dicionario das corretas pra fazer o envio
        corretas = {}
        corretas['corretas'] = ['roberto pula o caminhao']
        #ele tem a chave corretas,que é uma lista com as alternativas
        #corretas a adicionar
        
        #acrescento uma vez, com sucesso
        r = requests.put(url+'questao/1/corretas', json = corretas)
        self.assertEqual(r.status_code,200)
       
        #ao consultar a função, temos a nova alternativa, 
        #e a lista de alternativas agora tem tamanho 2
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['corretas']),2)
        self.assertEqual(devolvida['corretas'][-1],'roberto pula o caminhao')

    
    def test_009b_adiciona_alternativas_corretas_em_uma_questao(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        #monto o dicionario das corretas pra fazer o envio
        corretas = {}
        corretas['corretas'] = ['roberto pula o caminhao']
        #ele tem a chave corretas,que é uma lista com as alternativas
        #corretas a adicionar
        
        #acrescento uma vez, com sucesso
        r = requests.put(url+'questao/1/corretas', json = corretas)
        self.assertEqual(r.status_code,200)
       
        #ao consultar a função, temos a nova alternativa, 
        #e a lista de alternativas agora tem tamanho 2
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['corretas']),2)
        self.assertEqual(devolvida['corretas'][-1],'roberto pula o caminhao')

        #tento colocar de novo
        r = requests.put(url+'questao/1/corretas', json = corretas)
        
        #mas a lista de corretas nao muda, ainda tem tamanho 2
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['corretas']),2)
    
    #tento adicionar alternativas em uma questao que nao existe
    def test_009c_adiciona_alternativas_corretas_404(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        corretas = {}
        corretas['corretas'] = ['roberto pula o caminhao']

        #se tento adicionar em uma questao que nao existe
        r = requests.put(url+'questao/3/corretas', json = corretas)
        #devo receber um status 404
        self.assertEqual(r.status_code,404)
    
    #o usuário tenta responder a uma pergunta
    #(leia o enunciado para entender esse teste,
    #na parte "Respondendo às perguntas")
    def test_010_responder(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        #o usuário marcio quer dar resposta 12
        r1 = {'usuario':'marcio',
              'resposta':12}
        #como podemos ver na linha abaixo, vamos responder a questão 2
        r = requests.put(url+'responder/2', json=r1)

        #queremos um cod de status de sucesso
        self.assertEqual(r.status_code,200)

        #ao pegar as respostas, vemos que agora marcio respondeu 2 perguntas
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido['marcio']),2)

        #se eu tentar mandar outra resposta para a mesma
        #pergunta, isso nao deve ter efeito
        r = requests.put(url+'responder/2', json=r1)
        #tomo um erro 409
        self.assertEqual(r.status_code,409)

        #e a lista de respostas nao sofreu alteração
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),2)
       
        #agora um usuário novo quer responder
        r2 = {'usuario':'don juan',
              'resposta':12}
        #ele faz o request
        r = requests.put(url+'responder/2', json=r2)
        #e recebe um cod status 200 (OK)
        self.assertEqual(r.status_code,200)
        #ao consultarmos a lista de respostas...
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        #... agora temos 3 usuários
        self.assertEqual(len(dic_recebido),3)
        #e o don respondeu a uma só pergunta
        self.assertEqual(len(dic_recebido['don juan']),1)
    
    def test_010a_responder_questao_invalida(self):
        #reseto as listas
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        #pego a lista de respostas
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        #e verifico quantas pessoas existem
        # e quantas questoes marcio respondeu
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),1)

        #nao consigo responder a questao 3, pois ela nao existe
        r1 = {'usuario':'marcio',
              'resposta':12}
        #ao tentar fazer o request
        r = requests.put(url+'responder/3', json=r1)
        #tomo um cod status 404
        self.assertEqual(r.status_code,404)
        #depois pego a lista de respostas
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        #e verifico que nada mudou. Ela ainda tem 2
        #pessoas, e marcio tem apenas 1 resposta, como
        #era desde o inicio
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),1)
        
        #agora crio a questao 3, e ai vai dar certo
        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)

        #minha segunda tentativa de responder a questao 3,
        #agora que ela existe
        r1 = {'usuario':'marcio',
              'resposta':12}
        r = requests.put(url+'responder/3', json=r1)
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        #veja que o numero de respostas do marcio aumentou
        self.assertEqual(len(dic_recebido['marcio']),2)


    #pego o resumo de desempenho da usuaria maria
    #se você olhar nos dicionarios definidos
    #no inicio do arquivo, verá que ela respondeu
    #todas as 2 questões, e acertou as duas
    def test_011_desempenho(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        r = requests.get(url+'maria/resultados')
        self.assertEqual(r.json()['usuario'],'maria')
        self.assertEqual(r.json()['acertos'],2)
        self.assertEqual(r.json()['erros'],0)
        self.assertEqual(r.json()['nao respondidas'],0)
        
    def test_011b_desempenho(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        r = requests.get(url+'marcio/resultados')
        self.assertEqual(r.json()['usuario'],'marcio')
        self.assertEqual(r.json()['acertos'],0)
        self.assertEqual(r.json()['erros'],1)
        self.assertEqual(r.json()['nao respondidas'],1)
    
    def test_011c_desempenho(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        r = requests.get(url+'marcio/resultados')
        self.assertEqual(r.json()['usuario'],'marcio')
        self.assertEqual(r.json()['acertos'],0)
        self.assertEqual(r.json()['erros'],1)
        self.assertEqual(r.json()['nao respondidas'],1)
        
        #o usuário marcio quer dar resposta 12
        r1 = {'usuario':'marcio',
              'resposta':12}
        #como podemos ver na linha abaixo, vamos responder a questão 2
        r = requests.put(url+'responder/2', json=r1)

        r = requests.get(url+'marcio/resultados')
        self.assertEqual(r.json()['usuario'],'marcio')
        self.assertEqual(r.json()['acertos'],0)
        self.assertEqual(r.json()['erros'],2)
        self.assertEqual(r.json()['nao respondidas'],0)

    def test_011d_desempenho(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        r = requests.get(url+'marcio/resultados')
        self.assertEqual(r.json()['usuario'],'marcio')
        self.assertEqual(r.json()['acertos'],0)
        self.assertEqual(r.json()['erros'],1)
        self.assertEqual(r.json()['nao respondidas'],1)
        
        #o usuário marcio quer dar resposta 12
        r1 = {'usuario':'marcio',
              'resposta':64}
        #como podemos ver na linha abaixo, vamos responder a questão 2
        r = requests.put(url+'responder/2', json=r1)

        r = requests.get(url+'marcio/resultados')
        self.assertEqual(r.json()['usuario'],'marcio')
        self.assertEqual(r.json()['acertos'],1)
        self.assertEqual(r.json()['erros'],1)
        self.assertEqual(r.json()['nao respondidas'],0)
        

    def test_100_id_crescente(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        r = requests.get(url+'questao/3')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['pergunta'],q1['pergunta'])
        


    
    def test_101_sem_ids_repetidas(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        q2 = {
            'pergunta': 'Quanto vale 3+4?',
            'erradas': [12,36,26,32],
            'corretas': [7]
        }
        r = requests.post(url+'questao',json = q2)
        self.assertEqual(r.status_code,201)
        q3 = {
            'pergunta': 'Whate is the brother?',
            'erradas': [12,36,26,32],
            'corretas': ['uma geracao marcante']
        }
        r = requests.post(url+'questao',json = q3)
        self.assertEqual(r.status_code,201)
    

        r = requests.get(url+'questoes')
        lista_retornada = r.json()
        self.assertTrue(len(lista_retornada) == 5)

        for dic in lista_retornada:
            self.assertIn('id',dic)

        ids = []
        for dic in lista_retornada:
            ids.append(dic['id'])
        if (len(set(ids)) != len(ids)):
            self.fail('existe alguma id repetida na sua lista de questoes!')



    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
