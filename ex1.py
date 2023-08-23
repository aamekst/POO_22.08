"""excercio 5 e 6"""
""" split = conta as plavras e olha pelo espaço"""
""" len = conta os itens da lista"""

def lista(frase):
    lista = frase.split(' ')
    return lista #separa as palavras

def conta(frase):
    lista= frase.split(' ')
    return len(lista) #quantas palavras tem

frase = input('Frase:')
print(lista(frase))
print(conta(frase))


