#replace retorna um copia, deica frase + frase para salva na variavel frase

def remove(frase):
    frase = frase.replace(' ', '') #remove o primeiro ' ' para o ''
    return frase

frase=input('Frase:')
print(remove(frase))