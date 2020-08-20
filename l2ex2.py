def menor_nome(nomes):
    indice_menor=0
    menor_tamanho=len(nomes[0].strip())
    for i in range(len(nomes)):
        nome=nomes[i].strip()
        if len(nome)<menor_tamanho:
            menor_tamanho==len(nome)
            indice_menor=i
        
    return nomes[indice_menor].strip().capitalize()
