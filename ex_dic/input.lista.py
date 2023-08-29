alunos = {}

for i in range(2):
    ra = input('CPF:')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    alunos[ra] = [n1, n2, n3]
print(alunos)