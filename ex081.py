lista = list()
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    r = input('Quer continuar? [S/N]').upper()
    for c in range(0, len(lista)):
        c = c + 1
    if r == 'N':
        break
print(f'O total de números digitados foi {c}')
lista.sort(reverse=True)
print(f'Os valores digitados foram: {lista}')
if lista.count(5) == 0:
    print('O valor não aparece na lista')
else:
    print('O valor está na lista!')
