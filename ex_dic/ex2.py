venda = {}

for i in range(3):
    produto = input('produto:')
    preco = int(input('preço: '))
    venda[produto] = preco

#percorre o dicionario verifica
for produto, preco in venda.items():
    if preco >= 50:
        print(f'preco: {preco}, Produto: {produto}')


