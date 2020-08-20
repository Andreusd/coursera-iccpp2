def imprime_matriz(matriz):
    for i in matriz:
        for j in range(len(i)):
            print(i[j],end='',sep='')
            if(j<len(i)-1):
                print(" ",end='')
        print()

def cria_matriz(num_linhas,num_colunas,valor):
    matriz=[]
    for i in range(1,num_linhas+1):
        linha=[]
        for j in range(1,num_colunas+1):
            linha.append(valor)
        matriz.append(linha)
    return matriz
