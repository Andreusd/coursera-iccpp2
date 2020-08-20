def soma_lista(lista):
    if lista:
        return lista[0]+soma_lista(lista[1:])
    else:
        return 0
