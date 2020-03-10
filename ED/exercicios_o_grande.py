#lembrar como funciona o range


def funcao_exemplo(a,b):
    for i in range(a):
        imprime(i)
        imprime(': ')
        for j in range(b):
            imprime(j)
            imprime(', ')
        nova_linha()


def funcao1(a,b):
    cont = 0
    for i in range(a):
        for j in range(b):
           cont = cont + 1 #marca!
    return cont
#questao 1: se a=10 e b=100, quantas vezes a linha marcada é executada?
#resposta: 1000
#questao 2: se a=20 e b=10, quantas vezes a linha marcada é executada?
#resposta: 200
#questao 3: se a=100 e b=10, quantas vezes a linha marcada é executada?
#resposta: 1000
#questao 4: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de a e b?
#resposta: range de a vezes range de b
def funcao2(a,b):
    cont=0
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    for i in range(a):
        for j in range(b):
            cont = cont+1 #marca!
    return cont
#questao 5: se a=10 e b=100, quantas vezes as linhas marcadas são executadas?
#resposta: 2000
#questao 6: se a=20 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 400
#questao 7: se a=100 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 2000
#questao 8: qual a formula que descreve o numero de execuções das linhas
    #marcadas em termos de a e b?
#resposta: range de a vezes range de b mais range de a
def funcao3(n):
    cont=0
    for i in range(n):
        cont = cont+1 #marca!
    for i in range(n):
        cont = cont+1 #marca!
    return cont
#questao 9: se n=10, quantas vezes as linhas marcadas são executadas?
#resposta: 20
#questao 10: se n=100, quantas vezes as linhas marcadas são executadas?
#resposta: 200
#questao 11: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n?
#resposta: 2 vezes range de n
#desafio 1: se a funcao3 demorou 10 segundos na minha máquina, com n=1000,
    #quantos segundos ela vai demorar com n=2000?
#resposta: 20 segundos
def funcao4(n):
    cont=0
    for i in range(n):
        for j in range(n):
           cont = cont+1 #marca!
    for i in range(n):
        cont = cont+1 #marca!
    return cont
#questao 12: se n=10, quantas vezes as linhas marcadas são executadas?
#resposta: 110
#questao 13: se n=100, quantas vezes as linhas marcadas são executadas?
#resposta: 10100
#questao 14: se n=1000, quantas vezes as linhas marcadas são executadas?
#resposta: 1001000
#questao 15: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n?
#desafio 2: se a funcao4 demorou 1 segundo na minha máquina, com n=10000,
    #quantos segundos ela vai demorar com n=20000?

def funcao5(a,b):
    cont=0
    for i in range(a):
        for j in range(a):
           cont = cont+1
    for i in range(b):
        cont = cont+1
    return cont
#questao 16: se a=10 e b=100, quantas vezes as linhas marcadas são executadas?
#resposta: 200
#questao 17: se a=20 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 410
#questao 18: se a=100 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 10010
#questao 20: qual a formula que descreve o numero de execuções das linhas
    #marcadas em termos de a e b?

def funcao6(a,b):
    cont=0
    for i in range(a):
        for j in range(a):
           cont = cont+1
    for i in range(b):
        for j in range(b):
           cont = cont+1
    for i in range(b):
        cont = cont+1
    return cont
#questao 21: se a=10 e b=100, quantas vezes as linhas marcadas são executadas?
#resposta: 10200
#questao 22: se a=20 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 510
#questao 23: se a=100 e b=10, quantas vezes as linhas marcadas são executadas?
#resposta: 10110
#questao 24: qual a formula que descreve o numero de execuções das linhas
    #marcadas em termos de a e b?

def funcao7(lista):
   i=0
   for e1 in lista:
        for e2 in lista:
             i = i+1 #marca!

#questao 25: se a lista tem tamanho 1000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 1000000    
#questao 26: se a lista tem tamanho 2000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 4000000    
#questao 27: se a lista tem tamanho 4000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 16000000
#questao 28: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n (n é o tamanho da lista)?
#desafio 3: se a funcao7 demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?
def funcao8(lista):
   i=0
   for e in lista:
         i = i+1 #marca!
#questao 29: se a lista tem tamanho 1000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 1000
#questao 30: se a lista tem tamanho 2000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 2000
#questao 31: se a lista tem tamanho 4000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 4000
#questao 32: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n (n é o tamanho da lista)?
#desafio 3: se a funcao8 demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?

def funcao9(lista):
   i=0
   for e in lista:
         i = i+1 #marca!
   for e1 in lista:
        for e2 in lista:
             i = i+1 #marca!
#questao 33: se a lista tem tamanho 1000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 1001000
#questao 34: se a lista tem tamanho 2000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 4002000
#questao 35: se a lista tem tamanho 4000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 16004000
#questao 36: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n (n é o tamanho da lista)?
#desafio 4: se a funcao9 demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?

def funcao10(lista):
   i=0
   for e in lista:
       for k in [0,1,2,3,4,5,6,7,8,9]:
         i = i+1 #marca!
#questao 37: se a lista tem tamanho 1000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 10000
#questao 38: se a lista tem tamanho 2000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 20000
#questao 39: se a lista tem tamanho 4000, 
    #quantas vezes as linhas marcadas são executadas?
#resposta: 40000
#questao 40: qual a formula que descreve o numero de execuções da linha
    #marcada em termos de n (n é o tamanho da lista)?
#desafio 5: se a funcao10 demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?
#resposta: 2 minutos
#desafio 6: uma funcao dá n*n/2 passos quando recebe uma lista
    #de tamanho n. Ela demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?
#desafio 7: uma funcao dá n*n + 100*n passos quando recebe uma lista
    #de tamanho n. Ela demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?
    
#desafio 8: uma funcao dá n/2 passos quando recebe uma lista
    #de tamanho n. Ela demorou 1 minuto na minha máquina, com n=1  milhao,
    #quantos minutos ela vai demorar com n=2 milhoes?

#final boss!
def procura_casal_22(lista):
    for i in lista:
        if 22-i in lista:
            return True
    return False
#desafio 9: essa funcao 
    #demorou 10 segundos na minha máquina, com n=1000,
    #quantos segundos ela vai demorar com n=2000?
#resposta: 20 segundos
'''
a partir daqui nao ha nada para voce ver.
'''

import random
import time
def gera_lista(nmax):
    return [1]*nmax

def escolhe_tamanho(valor_max_novo):
  global valor_max
  global lista
  valor_max = valor_max_novo
  print ('a lista agora tem '+str(valor_max)+' numeros dentro')
  print ('mude o numero usando a funcao escolhe_tamanho')
  lista = gera_lista(valor_max)

escolhe_tamanho(1000)


def simula():
   print('testando versao O(n**2)')
   start=time.process_time()
   for i in range(1,10):
      procura_casal_22(lista)
   end = time.process_time()
   return end-start








def imprime(string):
    print(string, end='')

def nova_linha():
    print('')
