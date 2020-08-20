def ordenada(lista):
    inicial = lista[0]
    for elemento in lista:
        if elemento < inicial:
            return(False)
    return(True)
