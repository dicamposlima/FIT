def anagramas(palavra):
    if not palavra:
        return [palavra]
    anagrama = []
    subanagramas = anagramas(palavra[1:])
    for letra in subanagramas:
        for indice in range(len(letra) + 1):
            myString = letra[:indice], ' ', palavra[0], ' ', letra[indice:]
            anagrama.append(letra[:indice] + palavra[0] + letra[indice:])
    return anagrama

anagramas('abc')