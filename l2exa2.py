def primeiro_lex(lista):
    menor=lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor
