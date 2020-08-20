def conta_letras(frase, contar="vogais"):
    quantidade_vogais=0
    quantidade_consoantes=0
    vogais = ('a','e','i','o','u')
    for letra in frase:
        if letra in vogais:
            quantidade_vogais+=1
        elif letra != ' ':
            quantidade_consoantes+=1
    if(contar=="vogais"):
        return quantidade_vogais
    else:
        return quantidade_consoantes
