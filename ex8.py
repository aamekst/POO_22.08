#append adcionar no final da lista
#max retorna o maior valor da lista
#min o menor numero
#sum a soma dos itens
#len quanta a quantidade de item
#range quando vc coloca o numero maximo como por ex 10, ele começara contando do 0
lista=[]
for i in range(10):
    num = int(input('Numero:'))
    lista.append(num)
print(lista)

maior= max(lista)
menor = min(lista)
media = sum(lista)/len(lista)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {media}')