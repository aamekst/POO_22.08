#DICIONARIO
#estrutura de dados, agrupamento de dados
#armezena coleção de itens, porém não sao organizados sequnciais e sim por CHVAES
#cada item terá duas duas informações (CHAVE E VALOR) 
#chave = 1 valor (unico), porém o valor pode ser uma lista

#chaves são imutaveis e unicas
#valores são  mutaveis
#dicionario pode existir em outro dicionario

dicionario = {'nome' : 'ana'}
print(dicionario)

#dicionario e dicionario
dicionario = {567 : {'nome': 'alana', 'work': 'nada'}}
print(dicionario)

#RA E NOME
alunos = {'1234': 'VITOR',
          '45678': 'BRUNA',
          '3456': 'AGATHA'}

print(alunos)

#CONSULTA chave especifica
print(alunos['1234'])

#ALTERA VALOR - chave existe
alunos['3456'] = 1223
print(alunos)

#inserir um novo aluno - chave inexistente
alunos['87698']= 'barbie'
print(alunos)

#remove um aluno - pop(chave) função usa ()
alunos.pop('1234')
print(alunos)

#operador IN (busca) - ["3456"]  - aspas dupla
if '3456' in alunos:
    print(f'yes: {alunos["3456"]}')
else:
    print('no')

#percorrer as chaves e valores
for valor in alunos.values():
    print(valor)

for valor in alunos.keys():
    print(valor)

#chave e valor - duas variaveis
for valor, chave in alunos.items():
    print(f'Nome: {valor}, Chave: {chave}')


#len tamanho do dicionario - quantos itens tem
print(len(alunos))

#preencher com input
'''alunos={}
for i in range(5):
    r = input('RA:')
    nome = input('nome: ')
    alunos[r] = nome 
print(alunos)'''


#lista 
alunos = {'1234': [9,7,8],
          '1030': [0,7,1],
          '1230': [9,10,10]}

#consulta
print(alunos['1234'][0]) # [0] - primeira nota (indice)

#altera
alunos['1234'][0] = 6 #posição
alunos['1234'] = [1,2,3] #tudo

#insere
alunos['1234'].append(10)
print(alunos)

#dicionario com dicionario 
dicionario = {567 : {'nome': 'alana', 'work': 'nada'},
              546 : {'nome': 'mario', 'work': 'encanamento'}}

#consulta - duas chave
print(dicionario[567]['nome'])


