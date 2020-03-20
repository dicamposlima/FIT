
'''
EXPLICACAO
Uma pilha é uma estrutura de dados que tem um "topo".

Ela guarda quantos elementos quisermos, mas só podemos ver/retirar
o elemento do topo.

Quando adicionamos um elemento, adicionamos no topo.

Em uma pilha a operação "colocar no topo" é chamada de "push",
e a operação "tirar do topo" é chamada de "pop".

Por exemplo:
    [] é uma pilha vazia.
    Se fizermos push(1), teremos a pilha [1] (1 no topo)
    Se fizermos push(2), push(5), teremos [1,2,5] (5 no topo)
    Se fizermos pop(), saiu o topo (5), e sobrou [1,2]
'''

'''
EXERCICIO
Continuando o exemplo, tinhamos [1,2].

Digamos que fazemos push(4), push(8). Como está a pilha? 
Responda na forma de uma lista na variavel pilha1
'''
pilha1=[1,2,4,8]

'''
EXERCICIO
Novo exemplo. Temos a pilha vazia []
Fazemos push(9),push(8),pop(),push(7),push(6),pop(). 

Como está a pilha? Responda na variavel pilha2.
'''
pilha2=[9,7]

'''
EXERCICIO
Novamente, começamos com uma pilha vazia.
E se fizermos 
push(9),push(8),push(7),push(6),pop(),pop(),pop() ?. 
'''
pilha3=[9]


'''
EXPLICACAO
Em python, podemos implementar o conceito de pilha usando uma lista, que têm as funções
append e pop

Por exemplo:

    >pilha = [] #inicializo uma pilha vazia
    >pilha.append(5)
    >pilha.append(8)
    >print(pilha)
    [5,8]
    >pilha.append(4)
    >pilha.append(3)
    >print(pilha)
    [5,8,4,3]
    >topo = pilha.pop()
    >print(topo)
    3
    >print(pilha)
    [5,8,4]

O append insere no final da lista e o pop tira do final da lista
'''

'''
EXERCICIO
Crie uma função poe_pilha, que recebe uma pilha e um número
e coloca o número no topo da pilha
'''
def poe_pilha(pilha,numero):
    return pilha.append(numero)

'''
EXERCICIO
Crie uma função tira_pilha, que recebe uma pilha, tira o número que
estava no topo e retorna ele

Exemplo: se a pilha era [1,2,3], a pilha deve ficar sendo [1,2] e a função deve retornar 3
'''
def tira_pilha(pilha):
    return pilha.pop()

'''
EXPLICAÇÃO

Dá pau tentar tirar uma coisa que não está na pilha.

Exemplo:

    > pilha = []
    > pilha.append(3)
    > topo = pilha.pop()
    > print(topo)
    3
    > topo = pilha.pop()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: pop from empty list

Para evitar esse problema, precisamos aprender a verificar se uma pilha está 
vazia.

Basta ver quantos elementos tem na lista. len faz exatamente isso.
    > pilha = []
    > pilha.append(30)
    > pilha.append(40)
    > pilha.append(50)
    > len(pilha)
    3   #pilha tem os 3 elementos: 30,40,50. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    50
    > len(pilha)
    2   #pilha tem 2 elementos: 30,40. Posso tirar um
    > topo = pilha.pop()
    > print(topo)
    40
    > len(pilha)
    1   #pilha tem 1 elemento: 30. Posso tirar ele
    > topo = pilha.pop()
    > print(topo)
    30
    > len(pilha)
    0   #pilha está vazia. Se eu tentar tirar algum elemento, vai dar pau
'''

'''
EXERCICIO
Faça uma função pilha_vazia que retorna:
     True se a pilha está vazia;
     False se não está
'''
def pilha_vazia(pilha):
    return len(pilha)==0


'''
EXERCICIO

Faça uma função pilha_letras, que recebe uma string e vai colocando as letras
da string uma a uma em uma pilha. A cada letra que for colocada, sua
função deve tirar uma fotografia da pilha (chamando a função
fotografa com sua pilha como argumento: fotografa(pilha)).
Não tire uma fotografia da pilha vazia

Sua função deve retornar a pilha pronta

Vou deixar um rascunho pra voce comecar

def pilha_letras(texto):
    for letra in texto:                            | cada vez com a variavel 'letra' 
        print(letra)      |  esse código é           sendo uma das letras do texto
        print('ola')      |  executado várias vezes

'''

def pilha_letras(texto):
    pilha=[]
    for letra in texto: 
        poe_pilha(pilha,letra)
        fotografa(pilha)
    return pilha

'''
EXERCICIO

Fazer uma função "menos_o_d". Ela recebe uma string e vai colocando as
letras uma a uma em uma pilha, como a funcao acima. Porém, quando ela vê uma
letra d, ao invés de colocar o d, ela faz um pop() na pilha, tirando a ultima letra
logo antes do d.

Tire uma fotografia sempre que inserir ou retirar uma letra. Não fotografe a pilha vazia
inicial (mas se surgirem outras no meio da execução, voce pode e deve fotografar)

Sua função deve retornar a ultima pilha
'''

def menos_o_d(texto):
    pilha=[]
    for letra in texto: 
        if letra == 'd':
            if not pilha_vazia(pilha):
                tira_pilha(pilha)
        else:    
            poe_pilha(pilha,letra)
        fotografa(pilha)
    return pilha

'''
EXERCICIO: Uma coisa estranha da função menos_o_d, que talvez você tenha notado,
é que se a primeira letra for d, ela talvez tente tirar uma coisa de uma pilha vazia.

Outro caso ruim seria a string 'addd', que empilha um a, depois tira, 
depois tenta tirar de novo (2 vezes!)

Nesses casos ruins, faça o seguinte: se a pilha está vazia e veio um "d", simplesmente
não tire nada da pilha. Ela continuará vazia.

(esse exercício é um "upgrade" na função menos_o_d. Mude ela!)
'''
'''
EXERCICIO

Estamos quase prontos para fazer o exercicio principal da aula, a função
'balanceado'.

Primero, vamos fazer uma funcao que verifica se um determinado "abre" 
encaixa com um "fecha".

Por exemplo, "(" encaixa com ")", mas não encaixa com "]", "}", nem "(", nem "["
Por exemplo, "[" encaixa com "]", mas não encaixa com ")", "}", nem "(", nem "["
Na verdade, "(" só encaixa com ")", "[" só encaixa com "]" e "{" só encaixa com "}"

Faça uma função encaixa, que recebe duas strings, um "abre" e um "fecha", e retorna
True se eles encaixam (False se não encaixarem)
'''
def encaixa(abre, fecha):
    if abre == '{' and fecha == '}':
        return True
    if abre == '[' and fecha == ']':
        return True
    if abre == '(' and fecha == ')':
        return True
    if abre == '<' and fecha == '>':
        return True
    return False    

'''
EXPLICACAO
Uma sequencia de parenteses "(" ")", colchetes "[" "]" e chaves "{" "}" 
é dita balanceada se cada simbolo "aberto" é "fechado" 
em um momento apropriado 

Por exemplo
'([])' é uma sequencia balanceada
'([)]' não é balanceada
'([]' não é balanceada
')' não é balanceada
'' é balanceada

Como já discutimos, esse problema é interessante porque
tem uma correspondencia com o problema de validar um arquivo html,
onde as tags html abrem e fecham, como os parenteses.

De uma olhada no arquivo pilhas_simulacao para relembrar
como o algoritmo proposto deve funcionar.
'''

'''
EXERCICIO RESOLVIDO. 

De uma olhada no arquivo pilhas_simulacao para relembrar
como o algoritmo proposto deve funcionar.

Agora, considere a seguinte string balanceada: '(()[a])'

Como vimos, o algoritmo vai lendo caractere a caractere
e atualizando a pilha. O que está na pilha, quando o 
algoritmo lê a letra "a"? 

Vou deixar esse respondido pra você ver o que é esperado

pilha_respondida=['(','[']

O que aconteceu a história da pilha foi a seguinte:
    []
    ['(']
    ['(','(']
    ['('] (um '(' foi retirado para encaixar com o ')'
    ['(','[']
'''    

'''
EXERCICIO

Agora, considere a seguinte string balanceada: '(([]{a}))'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada1
'''
pilha_balanceada1=['(','(','{']
'''
EXERCICIO

Agora, considere a seguinte string balanceada: '{}[](a)'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada2
'''
pilha_balanceada2=['(']
'''
EXERCICIO

Agora, considere a seguinte string balanceada: '()(()[]{a})'

O que está na pilha, quando o algoritmo lê a letra "a"? 

Responda na variável pilha_balanceada3
'''
pilha_balanceada3=['(','{']

'''
EXERCICIO

Escreva uma funcao "balanceada" que recebe uma string e
retorna "True" se a string representa uma sequencia balanceada, 
"False" caso contrário.

Não deixe de olhar o arquivo pilhas_simulacao para entender/relembrar 
como o algoritmo deve funcionar

Sua função só vai receber parênteses, colchetes e chaves.
Não precisa se preocupar com nenhum outro caractere
'''


def balanceada(string):
    pilha=[]
    length=0
    allowed_values=['(',')','{','}','[',']','<','>']
    for letra in string: 
        if not pilha_vazia(pilha) and encaixa(pilha[-1],letra):
            tira_pilha(pilha)
        elif letra in allowed_values:  
            poe_pilha(pilha,letra)
            if len(pilha)>length:
                length=len(pilha)
    if pilha_vazia(pilha):
        fotografa(length)
    return pilha_vazia(pilha)
'''
EXERCICIO

Podemos fazer alguns upgrades na funcao balanceada:
    * Além de aceitar (, [ e {, queremos que ela aceite <, que será fechado com >
    * Se vier alguma letra/numero (ou qualquer outra coisa que nao seja (){}[]<> a funcao
    deve ignorar ao invés de dar pau
    * Se a string for balanceada, a funcao deve calcular qual foi o **maximo** 
    tamanho da pilha. Esse valor deve ser "fotografado" uma unica vez, 
    no final da execucao. Sugiro que você vá calculando, sem saber se a string
    é balanceada ou não, mas tire a fotografia uma linha antes do "return true"
'''


'''
EXERCICIO
IMPLEMENTE A PROXIMA FUNCAO USANDO PILHAS


Defina uma função palindromo, 
que recebe uma string e retorna
True se ela é um palindromo, False caso contrario.

Um palindromo é uma string "espelhada"

Por exemplo palindromo('abbabba') retorna True
Por exemplo palindromo('aaa') retorna True
Por exemplo palindromo('aaaa') retorna True
Por exemplo palindromo('aac') retorna False
Por exemplo palindromo('a') retorna True
Por exemplo palindromo('') retorna True

dicas:
    Usando pilhas, podemos "empilhar" até a metade da string,
    depois "desempilhar" e ir verificando se o caracter desempilhado
    corresponde ao proximo caracter da string.

    Por exemplo, ao recebermos 'abbccbba'

    Empilhamos os primeiros 4 (a pilha fica 'abbc')
    damos pop() (o resultado é c) e comparamos com o proximo caractere (c)
    damos pop() (o resultado é b) e comparamos com o proximo caractere (b)
    damos pop() (o resultado é b) e comparamos com o proximo caractere (b)
    damos pop() (o resultado é a) e comparamos com o proximo caractere (a)

    Assim, a string é um palindromo
    
'''
def palindromo(string):
    metade  = int((len(string)/2))
    metade1 = []
    metade2 = []
    letras = []
    for letra in string:
        letras.append(letra)
    metade1 = letras[0:metade]
    metade2 = letras[metade:] if len(string) % 2 == 0 else letras[metade+1:]
    metade2.reverse()
    return metade1 == metade2

'''
EXERCICIO

Implemente uma classe pilha que dá suporte a 6 operações:
    *push (coloca um elemento na pilha)
    *pop (retira o elemento do topo e o retorna)
    *tamanho (verifica quantos elementos existem na pilha)
    *vazia (retorna True se a pilha está vazia, False caso contrário)
    *top (retorna o elemento do topo sem alterar a pilha)

    Já vou te fornecer parte do código. Depois do código, tem uma descricao de 
    como testar
'''

class Pilha():

    def __repr__(self):
        return str(self.lista)

    def __init__(self):
        self.lista = []

    def push(self,elemento):
        self.lista.append(elemento)

    def pop(self):
        return self.lista.pop()

    def tamanho(self):
        return len(self.lista)

    def top(self):
        return self.lista[-1]

    def vazia(self):
        return self.tamanho()==0

'''
    Veja abaixo como usar os métodos já fornecidos

    > p = Pilha() #cria uma nova pilha
    > p.push(2) #coloca o 2 na pilha
    > p.push(3) #coloca o 3 na pilha
    > p.pop()
    3
    > p.pop()
    2

    O exercicio consiste em implementar os outros métodos
'''


import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_001_var_pilha1(self):
        self.verifica_pilha(pilha1,'30683e81e541f4f031f50134b6c4df4fb2325fb6222265fffa004832')
    def test_002_var_pilha2(self):
        self.verifica_pilha(pilha2,'12f16a9f7220b8fbba114ca53fa589d2137060e48ef51f87ede96a7d')

    def test_003_var_pilha3(self):
        self.verifica_pilha(pilha3,'fc53f829aced039d8170455b2e1b24e1fa08bebfd5457257832257a4')

    def test_010_poe_pilha(self):
        pilha_teste1 = [2,3]
        poe_pilha(pilha_teste1,4)
        self.assertEqual(pilha_teste1,[2,3,4])
        poe_pilha(pilha_teste1,5)
        self.assertEqual(pilha_teste1,[2,3,4,5])
        pilha_teste2 =[]
        poe_pilha(pilha_teste2,5)
        self.assertEqual(pilha_teste2,[5])
    
    def test_011_tira_pilha(self):
        pilha_teste3 = [1,2,3,4,5,6,7]
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,7)
        self.assertEqual(pilha_teste3,[1,2,3,4,5,6])
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,6)
        self.assertEqual(pilha_teste3,[1,2,3,4,5])
        topo = tira_pilha(pilha_teste3)
        self.assertEqual(topo,5)
        self.assertEqual(pilha_teste3,[1,2,3,4])

    def test_012_pilha_vazia(self):
        pilha_teste4 = [1,2,3]
        vazia =[]
        self.assertTrue(pilha_vazia(vazia))
        self.assertFalse(pilha_vazia(pilha_teste4))

    def test_013_pilha_letras(self):
        pilha_dada_por_aluno = pilha_letras('banana')
        correto = ['b', 'a', 'n', 'a', 'n', 'a']
        self.assertEqual(pilha_dada_por_aluno,correto)


    def test_014_pilha_letras_verifica_fotos(self):
        reseta_fotos()
        pilha_letras('banana')
        album_correto = [['b'], ['b', 'a'], ['b', 'a', 'n'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]
        album_execucao_da_funcao = fotografias


        if album_correto != album_execucao_da_funcao:
            print('Passei para sua função a palavra "banana".')
            print('Ela funcionou, mas não tirou as fotografias corretas')
            explica_erro(album_execucao_da_funcao,album_correto)
            self.fail('erro nas fotografias')

    def test_015_menos_o_d(self):
        pilha_dada_por_aluno = menos_o_d('banana')
        correto = ['b', 'a', 'n', 'a', 'n', 'a']
        self.assertEqual(pilha_dada_por_aluno,correto)
        pilha_dada_por_aluno = menos_o_d('bandana')
        correto = ['b', 'a', 'a', 'n', 'a']
        self.assertEqual(pilha_dada_por_aluno,correto)
    
    def test_016_menos_o_d_verifica_fotos(self):
        reseta_fotos()
        menos_o_d('bandana')
        album_correto = [['b'], ['b', 'a'], ['b', 'a', 'n'], ['b', 'a' ], ['b', 'a', 'a'] ,['b', 'a', 'a', 'n'], ['b', 'a', 'a', 'n', 'a']]
        album_execucao_da_funcao = fotografias


        if album_correto != album_execucao_da_funcao:
            print('Passei para sua função a palavra "bandana".')
            print('Ela funcionou, mas não tirou as fotografias corretas')
            explica_erro(album_execucao_da_funcao,album_correto)
            self.fail('erro nas fotografias')
        reseta_fotos()
        menos_o_d('adbdcd')
        album_correto = [['a'], [], ['b'], [], ['c'] ,[]]
        album_execucao_da_funcao = fotografias


        if album_correto != album_execucao_da_funcao:
            print('Passei para sua função a palavra "adbdcd".')
            print('Ela funcionou, mas não tirou as fotografias corretas')
            explica_erro(album_execucao_da_funcao,album_correto)
            self.fail('erro nas fotografias')
    
    def test_017_upgrade_menos_o_d(self):
        pilha_dada_por_aluno = menos_o_d('addd')
        correto = []
        self.assertEqual(pilha_dada_por_aluno,correto)
        pilha_dada_por_aluno = menos_o_d('dbandana')
        correto = ['b', 'a', 'a', 'n', 'a']
        self.assertEqual(pilha_dada_por_aluno,correto)

    def test_018_encaixa(self):
        self.assertTrue(encaixa('(',')'))
        self.assertTrue(encaixa('[',']'))
        self.assertTrue(encaixa('{','}'))
        self.assertFalse(encaixa('{',')'))
        self.assertFalse(encaixa('{',']'))
        self.assertFalse(encaixa('{','{'))
        self.assertFalse(encaixa('(',']'))
        self.assertFalse(encaixa('(','}'))
        self.assertFalse(encaixa('(','('))
        self.assertFalse(encaixa('[','}'))

    def test_020_pilha_balanceada1(self):
        self.verifica_pilha(pilha_balanceada1,'d05014e01b5592cef47539758e813503f58c743512164f6021ee62ac')
    
    def test_021_pilha_balanceada2(self):
        self.verifica_pilha(pilha_balanceada2,'53edf5c1b62d1568ba48e5f9ae4c65790a60a7084c91e6afbf600471')
    
    def test_023_pilha_balanceada3(self):
        self.verifica_pilha(pilha_balanceada3,'45ec24251c4b6f1be75226ba5bc896de21a0d4100de755ea870268e6')

    def test_024_primeiros_exemplos_balanceado(self):
        self.assertEqual(balanceada('([])'),True)
        self.assertEqual(balanceada('([]{})'),True)
        self.assertEqual(balanceada('([][])'),True)
        self.assertEqual(balanceada('([}[])'),False)
        self.assertEqual(balanceada('([}{])'),False)
        self.assertEqual(balanceada('([}{])'),False)
    
    def test_025_balanceado_mais_complexo(self):
        self.assertEqual(balanceada('([]'),False)
        self.assertEqual(balanceada('('),False)
        self.assertEqual(balanceada('((('),False)
        self.assertEqual(balanceada(')'),False)
        self.assertEqual(balanceada('(()))'),False)
        self.assertEqual(balanceada(''),True)

    def test_026_balanceado_upgrade_parenteses_angulares(self):
        self.assertEqual(balanceada('([]<>)'),True)
        self.assertEqual(balanceada('(<>{})'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('([}<>)'),False)
        self.assertEqual(balanceada('([><])'),False)
        self.assertEqual(balanceada('(<}{>)'),False)
        self.assertEqual(balanceada('<[]'),False)
        self.assertEqual(balanceada('<'),False)
        self.assertEqual(balanceada('>'),False)
    
    def test_027_balanceado_upgrade_letras_aleatorias(self):
        self.assertEqual(balanceada('([a]a<>i)'),True)
        self.assertEqual(balanceada('(<>g{g}j)'),True)
        self.assertEqual(balanceada('<[][]>'),True)
        self.assertEqual(balanceada('g(g[g}<>)'),False)

    def test_028_balanceado_contabilizou_maximo(self):
        reseta_fotos()
        balanceada('((()))')
        try:
            fotografias[0]
        except:
            self.fail('eu esperava uma fotografia, quando executei balanceada da string ((()))')
        reseta_fotos()
        balanceada('((()))')
        self.assertEqual(fotografias[0],3)
        reseta_fotos()
        balanceada('((()[]{}))')
        self.assertEqual(fotografias[0],3)
        reseta_fotos()
        balanceada('()[]{}')
        self.assertEqual(fotografias[0],1)



    
    def test_030_palindromo_comprimentos_pares(self):
        self.assertEqual(palindromo('aaaa') , True)
        self.assertEqual(palindromo('ac') , False)
        self.assertEqual(palindromo('abcddcba') , True)
        self.assertEqual(palindromo('abcdecba') , False)


    def test_031_palindromo_comprimentos_impares(self):    
        self.assertEqual(palindromo('abbabba'), True)
        self.assertEqual(palindromo('aaa') , True)
        self.assertEqual(palindromo('aac') , False)
        self.assertEqual(palindromo('abcdedcba') , True)

    def test_032_palindromo_peq(self):    
        self.assertEqual(palindromo('a') , True)
        self.assertEqual(palindromo('') , True)
    
    def test_040_classe_pilha_tamanho(self):
        p = Pilha()
        self.assertEqual(p.tamanho(),0)
        p.push(10)
        self.assertEqual(p.tamanho(),1)
        p.push(29)
        self.assertEqual(p.tamanho(),2)
        topo = p.pop()
        self.assertEqual(p.tamanho(),1)
    
    def test_041_classe_pilha_topo(self):
        p = Pilha()
        p.push(10)
        self.assertEqual(p.top(),10)
        p.push(29)
        self.assertEqual(p.top(),29)
        topo_antigo = p.pop()
        self.assertEqual(p.top(),10)
    
    def test_042_classe_pilha_vazia(self):
        p = Pilha()
        self.assertTrue(p.vazia())
        p.push(10)
        self.assertFalse(p.vazia())
        p.push(29)
        self.assertFalse(p.vazia())
        topo_antigo = p.pop()
        self.assertFalse(p.vazia())
        topo_antigo = p.pop()
        self.assertTrue(p.vazia())

    def verifica_pilha(self,pilha,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(pilha).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno,codigo_correto)
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)



fotografias = []
def reseta_fotos():
    global fotografias
    fotografias = []

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


