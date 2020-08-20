def maiusculas(frase):
    frase_maiusculas=""
    for letra in frase:
        if ord(letra) >=65 and ord(letra) <=90:
            frase_maiusculas+=letra
    return frase_maiusculas
