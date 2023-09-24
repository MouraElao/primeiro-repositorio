lista = list()
lista1 = list()
lista2 = list()
notas = list()
notas2 = list()
totp = 0
while True:
    totp = totp + 1
    nome = input(f'Nome {totp}: ').upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    lista.append(media)
    lista1.append(lista[:])
    lista2.append(lista[1])
    lista.clear()
    notas2.append(notas[:])
    notas.clear()
    r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 26)
for i, l in enumerate(lista2):
    print(f' {i:<4} {lista1[i][0]:<10}{l:>8.1f}')
    i = i + 1
while True:
    r = input('Quer saber as notas de algum aluno? [S/N]')
    if r in 'Nn':
        break
    r1 = int(input('De qual aluno?'))
    print(notas2[r1])

