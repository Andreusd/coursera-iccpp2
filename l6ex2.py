def encontra_impares(lista):
    if lista:
        e = lista.pop(0)
        if e % 2 != 0:
            return [e] + encontra_impares(lista)
        return encontra_impares(lista)
    else:
        return []
