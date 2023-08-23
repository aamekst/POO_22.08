lista = [] 
for i in range (5):
    numero = int (input('numero: '))
    lista.append(numero)
print(lista)

tupla = tuple(lista)            #copia os itens da lista para uma tupla
print(tupla)