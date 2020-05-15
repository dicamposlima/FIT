### Solução 1:
# Dê uma descrição do funcionamento desse algoritmo. 
# Algo como: lê uma peça da lista, verifica se pode utilizá-la no jogo. Se puder, encaixa ela no início...

# Qual parece ser a complexidade? O(n)? O(n**2)?

# Dê características ao código. É um código legível? Por quê? É um código curto? É um código rápido? 
# Qualquer característica que utilizar, explique os motivos.

### Resposta
# Primeiro duas listas são inicializadas, vazias, uma para o jogo e outra para as peças que sobram.
# Um for é inicializado, ele faz um loop por números que vão de n-1 até 0, o que indica uma complexidade de O(n)
# Dentro do loop há uma verificação, se o jogo ainda está vazio, uma ação será realizada, caso contrário, a ação será diferente.
# Caso o jogo ainda esteja vazio: adiciona a peça que está na posição x do vetor de entrada pecas e remove ela desse vetor.
# Caso o jogo já tenha alguma peça: verifica se a peça no início do vetor do jogo encaixa na última peça do vetor de entrada pecas. 
#   Se encaixar, insere a peça no início do vetor do jogo e remove a peça do vetor de input. 
#   Se não encaixar, insere a peça na lista de peças sobrando e remove a peça do vetor de input.

# Este código funciona porque será verificada cada uma das peças do vetor de entrada, 
# e se ela encaixar será colocada no vetor do jogo, na posição correta. 
# Se não encaixar será descartada no vetor de peças sobrando.

# Este código tem prints que foram deixados no código. Isso nunca é uma boa prática.
# O passo de remover a peça do vetor pecas é desnecessário, e acaba apenas dificultando a legibilidade.
# Também, um loop que vai da última posição até a primeira de um range acaba sendo mais verboso e um pouco mais difícil de acompanhar,
# talvez fosse mais interessante pensar em uma estratégia que seguisse o loop de frente para trás.

# O código consegue devolver de forma rápida e prática um jogo grande válido, mas para a função ser mais completa, 
# ela poderia ter verificado se a peça encaixa no final do jogo ou se é possível encaixar invertendo a peça.
# Também poderia ser verificado se não há alguma peça no vetor de peças sobrando que ainda pudesse ser encaixada, testando as peças até nenhuma encaixar.
# Uma estratégia que testa até a exaustão não teria complexidade O(n)

def jogo_grande(pecas):
    jogo_grande = list()
    pecas_sobrando = list()
    for x in range(len(pecas)-1, -1, -1):     
        if len(jogo_grande) == 0:
            jogo_grande.append(pecas[x])
            pecas.remove(pecas[x])          
        elif len(jogo_grande) >= 1:
            if jogo_grande[0].esquerda == pecas[x].direita:
                jogo_grande.insert(0, pecas[x])
                print(jogo_grande)
                pecas.remove(pecas[x])
            else:
                pecas_sobrando.append(pecas[x])
                pecas.remove(pecas[x])
    print(pecas_sobrando)
    return jogo_grande, pecas_sobrando




### Solução 2:
# Dê uma descrição do funcionamento desse algoritmo. 
# Algo como: lê uma peça da lista, verifica se pode utilizá-la no jogo. Se puder, encaixa ela no início...

# Qual parece ser a complexidade? O(n)? O(n**2)?

# Dê características ao código. É um código legível? Por quê? É um código curto? É um código rápido? 
# Qualquer característica que utilizar, explique os motivos.

### Resposta
# Primeiro duas listas são inicializadas, uma para o jogo, que começa vazia, e outra para as peças que sobram, que é inicializada com o input pecas.
# No primeiro passo a primeira peça do vetor do que está sobrando é inserida no jogo e removida do vetor de peças sobrando.
# Um while True cria um loop, com uma flag 'continuar' para indicar se o loop deve acabar e que, a princípio, está com o valor false, para terminar a execução.
# Dentro desse while há um for que será executado len(pecas_sobrando) vezes.
# Dentro do for, a função jogador é utilizada para verificar se a peça encaixa, e em qual posição ela encaixa.
# Se a peça não encaixar, ele segue o for.
# Se a peça encaixar, ele marca a flag 'continuar', pois encontrou uma peça neste loop, 
# e adiciona a peça na posição correta do jogo, a posição informada pela função jogador.
# Ao final do for, a peça inserida é removida da lista de peças sobrando.

# O código funciona porque ele verificará no máximo len(pecas) vezes se alguma peça encaixa no jogo, e adiciona cada peça que conseguir encaixar.
# Mas quando ele não consegue encontrar nenhuma peça que encaixa, ele decide que não será mais possível continuar e encerra o loop.
# Como a verificação de peças que encaixam custa, no máximo, len(pecas), e vimos que o while externo executa len(pecas), também no máximo, 
# isso mostra que o código tem complexidade O(n**2).

# Este código realiza todas as verificações pedidas no enunciado, e dificilmente seria realizado com uma complexidade menor.
# Ele utiliza as funções que haviam sido implementadas previamente, o que é ótimo para manutenção.
# O uso de while True, e flags de parada com break e continue, fazem o código perder legibilidade, e poderia ter sido tentado evitar.
# Porém, se o while e as flags fossem evitadas, dificilmente se manteria o código curto e sucinto.


def jogo_grande(pecas):
    pecas_sobrando = pecas
    jogo_grande = []
    jogo_grande.append(pecas_sobrando[0])
    pecas_sobrando.remove(pecas_sobrando[0])
        
    while True:
        continuar = False
        for i in range(len(pecas_sobrando)):
            jogada = jogador(jogo_grande, pecas_sobrando[i])
            
            if jogada == False:
                continue
            
            continuar = True    

            if jogada == 'frente':
                jogo_grande.append(pecas_sobrando[i])
            
            if jogada == 'atras':
                jogo_grande.insert(0, pecas_sobrando[i])

            pecas_sobrando.remove(pecas_sobrando[i])
            break

        if not continuar:
            break

    return jogo_grande,pecas_sobrando





### Solução 3:
# Dê uma descrição do funcionamento desse algoritmo. 
# Algo como: lê uma peça da lista, verifica se pode utilizá-la no jogo. Se puder, encaixa ela no início...

# Qual parece ser a complexidade? O(n)? O(n**2)?

# Dê características ao código. É um código legível? Por quê? É um código curto? É um código rápido? 
# Qualquer característica que utilizar, explique os motivos.

# Primeiro duas listas são inicializadas, uma para o jogo, que começa vazia, e outra para as peças que sobram, que é inicializada com o input pecas.
# Um for que percorre todo o input pecas é definido, sendo que seu primeiro passo é a verificação do jogo estar vazio.
# Se o jogo está vazio ele insere a primeria peça do input no jogo e remove essa peça do pecas_sobrando.
# Se o jogo não está vazio ele define um novo for para pecas_sobrando, o que sugere O(n**2).
# Dentro do for, a função jogador é utilizada para verificar se a peça encaixa, e em qual posição ela encaixa.
# Se a peça não encaixar, ele simplesmente segue a execução do for.
# Se a peça encaixar, ele adiciona a peça na posição correta do jogo, a posição informada pela função jogador.
# Ao final do for, se uma peça foi inserida, ela é removida da lista de peças sobrando.

# O código funciona porque ele fará len(pecas) vezes um loop que percorre cada peça em pecas_sobrando.
# O loop que percorre as peças de pecas_sobrando, simplesmente se utiliza da função jogador para inserir a peça no jogo.
# O loop externo pode ser executado um número de vezes com um pecas_sobrando que já foi validado, e se sabe que não pode mais ser utilizado.

# Este código realiza todas as verificações pedidas no enunciado, e dificilmente seria realizado com uma complexidade menor.
# Ele utiliza as funções que haviam sido implementadas previamente, o que é ótimo para manutenção.
# O código é amplamente legível e sucinto, e, apesar de já ter complexidade O(n**2), realiza passos desnecessários, 
# que poderiam ser evitados, o que reduz num fator muito pequeno o desempenho.
# Apesar disso teríamos que balancear, pois para melhorar o desempenho provavelmente prejudicaríamos a legibilidade.

def jogo_grande(pecas):

    jogo_grande = []
    pecas_sobrando = list(pecas)

    for v in pecas:
        if len(jogo_grande) == 0:
            jogo_grande.append(v)
            pecas_sobrando.remove(v)
            continue
        for v2 in pecas_sobrando:
            jogada = jogador(jogo_grande, v2)
            if jogada == 'frente':
                jogo_grande.append(v2)
            elif jogada == 'atras':
                no_comeco(jogo_grande, v2)
            if jogada is not False:
                pecas_sobrando.remove(v2)

    return jogo_grande,pecas_sobrando




### Solução 4:
# Dê uma descrição do funcionamento desse algoritmo. 
# Algo como: lê uma peça da lista, verifica se pode utilizá-la no jogo. Se puder, encaixa ela no início...

# Qual parece ser a complexidade? O(n)? O(n**2)?

# Dê características ao código. É um código legível? Por quê? É um código curto? É um código rápido? 
# Qualquer característica que utilizar, explique os motivos.

# Inicia-se duas listas vazias, uma para o jogo, outra para peças sobrando.
# Define-se um for que percorre o tamanho da lista de entrada, pecas.
# Dentro do for verifica-se se o x do loop é uma posição válida para a lista.
# Se for uma posição valida, verifica-se a peça nesta posição da entrada encaixa com a peça posterior.
# Se encaixar, a peça é colocada no jogo, caso uma peça não tenha sido removida no loop anterior. 
# Se não encaixar, a peça posterior é colocada como deletada e
# adicionada à lista de peças sobrando, além de adionar a peça atual à lista do jogo.

# Esse código está incorreto e passou nos testes por acaso. Se duas peças seguidas não encaixarem ele poderá adicionar peças que não encaixam.

def jogo_grande(pecas):
    jogo_grande = []
    pecas_sobrando = []
    bool = deletou = False
    for x in range(0,len(pecas),1):
        if ((x+1 < len(pecas))and(pecas[x].direita != pecas[x+1].esquerda)):
            pecas_sobrando.append(pecas[x+1])
            jogo_grande.append(pecas[x])
            deletou = True
        elif (deletou == False):
            jogo_grande.append(pecas[x])
        else:
            deletou = False
    return jogo_grande, pecas_sobrando




### Solução 5:
# Dê uma descrição do funcionamento desse algoritmo. 
# Algo como: lê uma peça da lista, verifica se pode utilizá-la no jogo. Se puder, encaixa ela no início...

# Qual parece ser a complexidade? O(n)? O(n**2)?

# Dê características ao código. É um código legível? Por quê? É um código curto? É um código rápido? 
# Qualquer característica que utilizar, explique os motivos.

# Esse código inicializa uma lista vazio para o jogo e uma para peças sobrando.
# A primeiro peça adicionada ao jogo é a primeira peça do input.
# Um for percorre cada peça do input
# Para cada peça do input, se a peça encaixar após a última peça do jogo válido, a peça será adicionada.
# Se não encaixar, a peça será colocada na lista das peças disponíveis.

# O código funciona porque gera uma lista válida de peças como um jogo.
# A complexidade é O(n) pois percorre apenas uma vez cada peça da entrada,
# porém não faz todas as verificações pedidas no enunciado.

# Ademais, está sucinto, legível e seguindo esta estratégia dificilmente seria mais rápido.

def jogo_grande(pecas):
    jogo = []
    pecas_disponiveis = []
    jogo.append(pecas[0])
    for p in range(1,len(pecas)):
        if jogo[-1].direita == pecas[p].esquerda:
            jogo.append(pecas[p])
        else:
            pecas_disponiveis.append(pecas[p])
    return jogo, pecas_disponiveis