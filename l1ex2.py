def dimensoes(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    return num_linhas, num_colunas

def soma_matrizes(m1,m2):
    if (dimensoes(m1)!=dimensoes(m2)):
        return False
    soma = []
    for i in range(len(m1)):
        linha=[]
        for j in range(len(m1[i])):
            linha.append(m1[i][j]+m2[i][j])
        soma.append(linha)
    return soma





matriz = [[1,2,3],[4,5,6],[7,8,9]]
