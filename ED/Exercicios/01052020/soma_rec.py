def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        primeiro_elemento = primeiro(lista)
        resto = demais_elementos(lista)
        return primeiro_elemento + soma(resto)


def soma0(lista):
    if len(lista) == 0:
        return 0


def soma1(lista):
    primeiro_elemento = primeiro(lista)
    resto = demais_elementos(lista)
    return primeiro_elemento + soma0(resto)


def soma2(lista):
    primeiro_elemento = primeiro(lista)
    resto = demais_elementos(lista)
    return primeiro_elemento + soma1(resto)


def soma3(lista):
    primeiro_elemento = primeiro(lista)
    resto = demais_elementos(lista)
    return primeiro_elemento + soma2(resto)


def soma4(lista):
    primeiro_elemento = primeiro(lista)
    resto = demais_elementos(lista)
    return primeiro_elemento + soma3(resto)


def soma5(lista):
    primeiro_elemento = primeiro(lista)
    resto = demais_elementos(lista)
    return primeiro_elemento + soma4(resto)


def primeiro(lista):
    return lista[0]


def demais_elementos(lista):
    return lista[1:]


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = int(len(lista) / 2)
    metade1 = lista[:meio]
    metade2 = lista[meio:]
    metade1 = mergesort(metade1)
    # a partir daqui, metade1 está ordenada
    metade2 = mergesort(metade2)
    # a partir daqui, metade2 está ordenada
    juntas = merge(metade1, metade2)
    return juntas


def merge(lista1, lista2):
    i = 0
    j = 0
    resposta = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resposta.append(lista1[i])
            i += 1
        else:
            resposta.append(lista2[j])
            j += 1
    while i < len(lista1):
        resposta.append(lista1[i])
        i += 1
    while j < len(lista2):
        resposta.append(lista2[j])
        j += 1
    return resposta
