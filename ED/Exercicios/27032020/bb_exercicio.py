
'''
EXERCICIO 

Considere a lista a seguir:
    [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]

Lembrando que as posicoes (indices) começam do 0, responda as perguntas a seguir 
corrigindo os valores das variaveis

1) Qual o indice do 20?
'''
indice_20=1

'''
2) Qual o indice do 400?
'''
indice_400=6
'''
3) Qual o indice do 5000?
'''
indice_5000=9
'''
Explicacao

Acessar um elemento de uma lista é fácil. É só usar colchetes, como
nos exemplos a seguir

    > lista = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
    > lista[0]
    100
    > lista[1]
    102
    > lista[3]
    106
'''

'''
EXERCICIO

   Faça uma funcao pega_indice, que recebe uma lista e um indice, e retorna
   o elemento que está nesse indice.

   Por exemplo,
   >>> lista = [100,102,105,990]
   >>> pega_indice(lista,2)
   105
'''
def pega_indice(lista,indice):
    return lista[indice]

'''
EXPLICACAO

Considere a função a seguir

0 def percorre(lista):
1    i = 0
2    while i < len(lista):
3        print('na posicao ',i,'temos o valor',lista[i])
4        i = i + 1
Ela imprime, para cada elemento da lista, sua posicao e o elemento em si.

Ela faz isso usando um while.

Por exemplo, se lista = [10,20,30], teremos 
* i = 0
* a linha 2 verifica que i < len(lista) (pois 0 < 3)
* como a condicao do while foi atentida, as linhas 3 e 4 sao executadas
* i = 1
* a linha 2 verifica que i < len(lista) (pois 1 < 3)
* como a condicao do while foi atentida, as linhas 3 e 4 sao executadas
...

'''
def percorre(lista):
    i = 0
    while i < len(lista):
        print('na posicao ',i,'temos o valor',lista[i])
        i = i + 1

lista20 = [20,21,22,23,24]
#percorre(lista20)
#descomente a linha acima para ver a funcao rodando

'''
EXERCICIO

    usando a mesma idéia do while acima, faça uma funcao que 
    busca um numero na lista, olhando indice a indice.

    Se o numero for encontrado, a funcao deverá retornar o indice

    Se o numero nao for encontrado, a funcao devera retornar false

'''

def busca_linear(lista, numero_a_procurar):
    i = 0
    while i < len(lista):
        fotografa((i,lista[i]))
        if lista[i] == numero_a_procurar:
            return i
        i = i + 1
    return False

'''
EXERCICIO

    Faça um upgrade da funcao anterior.

    Você deve fotografar o que está fazendo, da seguinte forma:

    Para cada i que você olhou, chame fotografa((i,lista[i]))

    Note os parenteses dobrados! É isso mesmo!
'''

'''
EXPLICACAO:

    Agora, vamos começar a pensar na busca binária. Ou seja, 
    começar a tentar fazer a busca mais rápida, "quebrando a lista na metade".

    A primeira coisa que temos que saber é calcular a posicao da metade de uma lista

    Dados dois números a e b, a média deles é (a+b)/2

    Por exemplo, a média de:
        *8 e 5 é (8+5)/2 = 6.5
        *8 e 6 é (8+6)/2 = 7
        *10 e 0 é (10+0)/2 = 5

    Coloque os valores das médias nas variáveis a seguir
'''
media_1_5 = 3
media_2_4 = 3
media_3_3 = 3

media_9_5 = 7


'''
EXPLICACAO:

    No nosso caso, nao queremos médias "de verdade", porque
    queremos escolher indices válidos.

    Assim, vejamos como calcular uma média "arredondada para baixo"
    > (12+20)//2
    16
    > (12+19)//2
    15

    O simbolo // significa divisao, mas jogando fora aquilo que vier depois
    da virgula.
'''

'''
Exercicio: Escreva uma funcao que recebe dois npumeros e devolve sua média
arredondada para baixo
'''

def media_arredondada(nro1, nro2):
    return (nro1+nro2)//2



'''
Lembra da busca binaria?

Se temos uma lista ORDENADA, e queremos saber se o 200 número está 
entre os indices 10 e 20.
podemos fazer o seguinte: 
1) Pegamos o indice do meio (15) e vemos qual número está lá.
2) Se achamos nosso numero, retornamos True
3) Caso o numero do meio seja maior que 200, 
so precisamos procurar na parte de tras da lista, entre os indices 10 e 14
4) Caso o numero do meio seja menor que 200, so precisamos procurar na parte da frente 
da lista: entre os indices 16 e 20
'''

'''
EXERCICIO
Agora, vamos usar essa a media_arredondada para consultar uma lista.


Façamos uma funcao numero do meio que recebe uma 
lista e dois indices, e devolve o numero na posicao do meio,
arredondando pra baixo se for o caso

por exemplo:
    >>> lista = [100,201,315,405,406,407,500,600,700,900,1000,1003]
    >>> numero_do_meio(lista,2,6)
    406

O que aconteceu?
Estamos considerando o intevalo do indice 2 ao 6
[100,201,315,405,406,407,500,600,700,900,1000,1003]
  0   1   2   3   4   5   6   7   8   9   10   11
         ___________________

O indice do número do meio é 4 (a média entre 2 e 6)
O número da lista que está nesse indice é o 406.

'''
def numero_do_meio(lista,comeco,fim):
    indice = media_arredondada(comeco,fim)
    return lista[indice]


'''
EXPLICACAO
Agora, façamos algumas pequenas simulações da busca binária.

Digamos que eu estou procurando o número 200.

No momento, acho que ele está entre o indice 20 e 30, se estiver na lista.
Isso quer dizer que eu vou verificar a posicao 25. Se achar o 215 na posicao
25, entao 200 só pode estar para trás. Devo procurar entre 20 e 24.

Vamos sintetizar esse resultado da sequinte forma: 25,(20,24)
Ou seja, escrever o indice que fomos olhar e os novos 2 indices onde nosso
número pode estar.
'''

'''
EXERCICIO
Digamos que eu estou procurando o número 200.

No momento, acho que ele está entre o indice 10 e 30, se estiver na lista.
Procurei no meio e achei o número 300.

Coloque os 3 números na proxima variável, como no exemplo acima
'''
busca1=20,(10,19)
'''
EXERCICIO
Digamos que eu estou procurando o número 200.

No momento, acho que ele está entre o indice 20 e 26, se estiver na lista.
Procurei no meio e achei o número 100.

Coloque os 3 números na proxima variável, como no exemplo
'''
busca2=23,(24,26)
'''
EXERCICIO
Digamos que eu estou procurando o número 200.

No momento, acho que ele está entre o indice 15 e 35, se estiver na lista.
Procurei no meio e achei o número 12.

Coloque os 3 números na proxima variável, como no exemplo
'''
busca3=25,(26,35)


'''
Agora que já vimos simulamos um passo da busca binaria, implementemos
um passo.

Façamos uma funcao passo_da_busca_binaria, que recebe 4 coisas:
    *uma lista
    *o numero a procurar
    *o menor indice
    *o maior indice

A idéia é que já eliminamos alguns pedaços da lista, de
forma que basta procurar o número entre o menor
e o maior indices.

Vamos achar o indice do meio, verificar se o número
que está lá é maior, menor ou igual ao que queremos.

Se ainda der pra procurar, retornaremos os novos indices maior
e menor (um deles mudou, por causa do jeito que a busca binaria 
funciona)

dica: return comeco,final #so deixei isso aqui pra voce lembrar como retornar 2 numeros

'''

def passo_da_busca_binaria(lista,procurando,menor_i,maior_i):
    comeco = menor_i
    final = maior_i
    valor_atual = numero_do_meio(lista,menor_i,maior_i)
    if valor_atual == procurando:
        comeco = media_arredondada(menor_i,maior_i)
        final = comeco
    elif valor_atual  > procurando:
        final = media_arredondada(menor_i,maior_i)-1
    else:
        comeco = media_arredondada(menor_i,maior_i)+1
    return comeco,final #so deixei isso aqui pra voce lembrar como retornar 2 numeros

'''
EXPLICACAO
Nosso proximo problema: se temos os dois indices, o do inicio e o do
fim do intervalo, quantos números ainda estão "sob suspeita" de 
serem o número procurado?

Olhando o exemplo a seguir, imagine que estamos procurando entre o
índice 2 e o 6.

[100,201,315,405,406,407,500,600,700,900,1000,1003]
  0   1   2   3   4   5   6   7   8   9   10   11
         ___________________

Nosso intervalo atual de busca contém 5 números (de 315 a 500)
'''
'''
EXERCICIO
Nas variaveis a seguir, indique o tamanho do intervalo.

Por exemplo, em t_intervalo_1_7, diga quantos números existem,
no intervalo que vai do indice 1 até o 7, incluindo
tanto o 1 quanto o 7
'''
t_intervalo_1_7 = 7
t_intervalo_5_8 = 4
t_intervalo_10_11 = 2
t_intervalo_2_1 = 0

'''
EXERCICIO
Crie uma funcao tam_do_intervalo(inicio,fim) que
conta quantos números ainda temos "sob suspeita"
'''
def tam_do_intervalo(inicio,fim):
    return max(fim-inicio+1,0)

'''
EXERCICIO

Estamos quase lá.

Façamos uma função passo_melhor_da_busca_binaria.

Quando o número ainda pode estar na lista, ela faz o mesmo que
o passo_da_busca_binaria: retorna o intervalo onde ele pode estar

Mas, quando ela acabou de ver o meio e achou o número, ela retorna True

E, quando ela já tem certeza que o número não está na lista 
(tamanho do intervalo é 0, ou é 1 mas o elemento não
é o procurado) ela retorna False
'''

def passo_melhor_da_busca_binaria(lista,procurando,menor_i,maior_i):
    menor_i,maior_i = passo_da_busca_binaria(lista,procurando,menor_i,maior_i)
    if menor_i == maior_i and lista[menor_i]==procurando:
        return True
    elif tam_do_intervalo(menor_i,maior_i) <= 1:
        return False
    return menor_i, maior_i
    


'''
EXERCICIO
Escreva uma funcao busca_binaria(lista,procurado)

Implementamos a ideia descrita acima da seguinte forma:
    Comecamos com duas variaveis, comeco = 0 e fim = len(lista)-1
    Definimos o meio como (comeco + fim)//2
    Verificamos se lista[meio] eh o numero que queremos.
    Se for, ja achamos 
    Se nao for, e o meio for maior, entao podemos pegar um novo fim: meio-1
    Se nao for, e o meio for menor, entao podemos pegar um novo comeco
'''
def busca_binaria(lista,procurado):
    menor_i = 0
    maior_i = len(lista)-1
    meio = media_arredondada(menor_i,maior_i)
    fotografa((meio,lista[meio]))
    while menor_i < maior_i:
        menor_i, maior_i = passo_da_busca_binaria(lista,procurado,menor_i,maior_i)
        meio = media_arredondada(menor_i,maior_i)
        fotografa((meio,lista[meio]))
        if menor_i == maior_i and lista[menor_i]==procurado:
            return True
        elif tam_do_intervalo(menor_i,maior_i) <= 1:
            return False
    return False

'''
EXERCICIO
Faça um upgrade na funcao busca_binária, tirando,
para cada número "do meio" que você consultar na lista, a fotografia a seguir:
    fotografa((meio,lista[meio]))

Note os parenteses dobrados. É assim mesmo!

Tome o cuidado de calcular o meio da forma sugerida -- (comeco+fim)//2 -- para
as fotografias baterem direitinho

'''




import unittest
import sys
import inspect
import hashlib

class TestStringMethods(unittest.TestCase):

    def test_000_indice_20(self):
        self.verifica_codigo(indice_20,'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178')
    def test_001_indice_400(self):
        self.verifica_codigo(indice_400,'31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26')
    def test_002_indice_5000(self):
        self.verifica_codigo(indice_5000,'192f56eb9bd894a72b30c303247b107be2c4591f310dd69a67927f48')

    def test_003_pega_indice(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        self.assertEqual(pega_indice(lista1,4),90)
        self.assertEqual(pega_indice(lista1,5),110)
        self.assertEqual(pega_indice(lista1,7),900)
        lista2 = [10, 20, 30, 40, 'orangotango', 110, 400, 900, 1000, 5000, 10000, 15000]
        self.assertEqual(pega_indice(lista2,4),'orangotango')

    def test_004_busca_linear(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        self.assertEqual(busca_linear(lista1,90),4)
        self.assertEqual(busca_linear(lista1,110),5)
        self.assertEqual(busca_linear(lista1,900),7)
        self.assertEqual(busca_linear(lista1,901),False)
        lista2 = [10, 20, 30, 40, 'orangotango', 110, 400, 900, 1000, 5000, 10000, 15000]
        self.assertEqual(busca_linear(lista2,'orangotango'),4)

    def test_005_busca_linear_fotografa(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        reseta_fotos()
        busca_linear(lista1,90)
        fotos_esperadas = [(0,10),(1,20),(2,30),(3,40),(4,90)]
        if fotografias != fotos_esperadas:
            print('Sua funcao funcionou, mas  não tirou as fotografias corretas')
            explica_erro(fotografias,fotos_esperadas)
            self.fail('erro nas fotografias')
        reseta_fotos()
        busca_linear(lista1,30)
        fotos_esperadas = [(0,10),(1,20),(2,30)]
        if fotografias != fotos_esperadas:
            print('Sua funcao funcionou, mas  não tirou as fotografias corretas')
            explica_erro(fotografias,fotos_esperadas)
            self.fail('erro nas fotografias')
    
    def test_006_media_1_5(self):
        self.verifica_codigo(media_1_5,'4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474')
    def test_007_media_2_4(self):
        self.verifica_codigo(media_2_4,'4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474')
    def test_008_media_3_3(self):
        self.verifica_codigo(media_3_3,'4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474')
    def test_009_media_9_5(self):
        self.verifica_codigo(media_9_5,'56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011')
    
    def test_010_media_arredondada(self):
        self.assertEqual(media_arredondada(5,7),6)
        self.assertEqual(media_arredondada(4,7),5)
        self.assertEqual(media_arredondada(4,6),5)
        self.assertEqual(media_arredondada(4,5),4)

    def test_011_numero_do_meio(self):
        lista = [100,201,315,405,406,407,500,600,700,900,1000,1003]
        self.assertEqual(numero_do_meio(lista,4,6),407)
        self.assertEqual(numero_do_meio(lista,3,7),407)
        self.assertEqual(numero_do_meio(lista,1,5),405)
        self.assertEqual(numero_do_meio(lista,0,5),315)

    def test_012_busca1(self):
        self.verifica_codigo(busca1,'d186920647502e420b2517c4014b1d1c923a8a962ec089db049c0307')
    def test_013_busca2(self):
        self.verifica_codigo(busca2,'500914115a9644c76ddd282251b5331e94168b082689874a30d4b345')
    def test_014_busca3(self):
            self.verifica_codigo(busca3,'ab032d3bfd46b4f346ef3f3ae487a3bb142cdb3264a762e689f33992')

    def test_015_passo_da_busca_binaria(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        comeco, fim = passo_da_busca_binaria(lista1,200,2,7)
        self.assertEqual(comeco,5)
        self.assertEqual(fim,7)
        comeco, fim = passo_da_busca_binaria(lista1,900,0,11)
        self.assertEqual(comeco,6)
        self.assertEqual(fim,11)
        comeco, fim = passo_da_busca_binaria(lista1,9,0,6)
        self.assertEqual(comeco,0)
        self.assertEqual(fim,2)
    
    def test_016_t_intervalo1(self):
        self.verifica_codigo(t_intervalo_1_7,'56929c1607626a1edbdaafb9c7f10c247e54fcbb20f1e3260f783011')
    def test_017_t_intervalo2(self):
        self.verifica_codigo(t_intervalo_5_8,'271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f')
    def test_018_t_intervalo3(self):
        self.verifica_codigo(t_intervalo_10_11,'58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9')
    def test_019_t_intervalo4(self):
        self.verifica_codigo(t_intervalo_2_1,'dfd5f9139a820075df69d7895015360b76d0360f3d4b77a845689614')

    def test_020_tam_do_intervalo(self):
        self.assertEqual(tam_do_intervalo(1,2),2)
        self.assertEqual(tam_do_intervalo(10,15),6)
        self.assertEqual(tam_do_intervalo(9,9),1)
        self.assertEqual(tam_do_intervalo(9,8),0)
        self.assertEqual(tam_do_intervalo(9,4),0)


    def test_021_passo_melhor_da_busca_binaria(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        comeco, fim = passo_melhor_da_busca_binaria(lista1,200,2,7)
        self.assertEqual(comeco,5)
        self.assertEqual(fim,7)
        comeco, fim = passo_melhor_da_busca_binaria(lista1,900,0,11)
        self.assertEqual(comeco,6)
        self.assertEqual(fim,11)
        comeco, fim = passo_melhor_da_busca_binaria(lista1,9,0,6)
        self.assertEqual(comeco,0)
        self.assertEqual(fim,2)

    def test_022_passo_melhor_da_busca_binaria2(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        resp = passo_melhor_da_busca_binaria(lista1,110,3,7)
        self.assertEqual(resp,True)
        resp = passo_melhor_da_busca_binaria(lista1,110,5,5)
        self.assertEqual(resp,True)
        resp = passo_melhor_da_busca_binaria(lista1,12,5,5)
        self.assertEqual(resp,False)

    def test_023_passo_melhor_da_busca_binaria3(self):
        lista1 = [10, 20, 30, 40, 90, 110, 400, 900, 1000, 5000, 10000, 15000]
        resp = passo_melhor_da_busca_binaria(lista1,12,5,4)
        self.assertEqual(resp,False)

    
    def verifica_codigo(self,valor_fornecido_aluno,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(valor_fornecido_aluno).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
    
    def test_024_busca_funciona(self):
        self.assertEqual(busca_binaria([0,1,2,3,4],2), True)
        self.assertEqual(busca_binaria([0,1,2,3,4],4), True)
        self.assertEqual(busca_binaria([0,1,2,3,4],5), False)
        self.assertEqual(busca_binaria([0,1,2,4,5,6,7,8],2), True)
        self.assertEqual(busca_binaria([0,1,2,4,5,6,7,8],3), False)
        self.assertEqual(busca_binaria([0,1,2,3,4,5,6],4), True)
        self.assertEqual(busca_binaria([0, 1, 2, 3, 4, 9, 10, 11, 12, 25, 32, 54, 56, 67, 72, 76, 87, 89, 100, 112, 400],5),False)
        self.assertEqual(busca_binaria([0, 101, 102, 103, 104, 109, 1010, 1011, 1012, 1025, 1032, 1054, 1056, 1067, 1072, 1076, 1087, 1089, 1100, 1112, 1400],500),False)
        self.assertEqual(busca_binaria([0, 101, 102, 103, 104, 109, 1010, 1011, 1012, 1025, 1032, 1054, 1056, 1067, 1072, 1076, 1087, 1089, 1100, 1112, 1400],5),False)

    def test_025_busca_fotografias(self):
        reseta_fotos()
        busca_binaria([0, 101, 102, 103, 104, 109, 1010, 1011, 1012, 1025, 1032, 1054, 1056, 1067, 1072, 1076, 1087, 1089, 1100, 1112, 1400],5)
        fotos_esperadas = [(10, 1032), (4, 104), (1, 101), (0, 0)]
        if fotografias != fotos_esperadas:
            print(fotografias)
            print('Sua funcao funcionou, mas  não tirou as fotografias corretas')
            explica_erro(fotografias,fotos_esperadas)
            self.fail('erro nas fotografias')
        reseta_fotos()
        busca_binaria([0, 101, 102, 103, 104, 109, 1010, 1011, 1012, 1025, 1032, 1054, 1056, 1067, 1072, 1076, 1087, 1089, 1100, 1112, 1400],500)
        fotos_esperadas = [(10, 1032), (4, 104), (7, 1011), (5, 109), (6, 1010)]
        if fotografias != fotos_esperadas:
            print(fotografias)
            print('Sua funcao funcionou, mas  não tirou as fotografias corretas')
            explica_erro(fotografias,fotos_esperadas)
            self.fail('erro nas fotografias')




    


    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


fotografias = []


def reseta_fotos():
    global fotografias
    while len(fotografias) > 0:
        fotografias.pop()

def fotografa(elemento):
    try:
        copia = elemento.copy()
    except:
        copia = elemento
    fotografias.append(copia)

def explica_erro(album1,album2):

    print('')

    if len(album1) == 0 and len(album2) > 0:
        print('Você não tirou nenhuma fotografia')
        print('Primeira fotografia esperada:')
        print(album2[0])
        return

    
    tam_do_menor = min(len(album1),len(album2))
    diferentes = [i for i in range(tam_do_menor) if album1[i] != album2[i]]
    if len(diferentes) > 0:
        menor_diferente = min(diferentes)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('Sua primeira fotografia errada:')
        print(album1[menor_diferente])
        print('Era esperado:')
        print(album2[menor_diferente])
        return

    if len(album1) < len(album2):
        print('Você tirou fotografias a menos')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album1)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que faltou:')
        print(album2[menor_diferente])

    if len(album1) > len(album2):
        print('Você tirou fotografias a mais')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album2)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que sobrou:')
        print(album1[menor_diferente])


runTests()