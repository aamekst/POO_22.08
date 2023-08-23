lista = []
for i in range(10):
    num = int(input('Numero:'))
    lista.append(num)
print(lista)

cont = 0            #contador
soma = 0            #somador

for item in lista:      #os itens da lista sao armazenados na variavel item do for
    if item % 2 == 0:
        cont += 1       #cont = cont + 1
    else:
        soma += item        #soma = soma + item
print(f'Quantidade de numeros pares: {cont}')
print(f'somatorio dos numeros impares: {soma}')