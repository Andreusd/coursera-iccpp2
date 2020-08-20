def ordena(lista):
    for i in range(len(lista)):
        trocando=i
        for j in range(1+i,len(lista)):
            if lista[trocando]>lista[j]:
                trocando=j
        lista[i],lista[trocando]=lista[trocando],lista[i]
    return lista


lista=[8,7,6,5,4,3]
