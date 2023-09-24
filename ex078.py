lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um número:')))
lista2 = lista[:]
lista.sort()
print(lista)
ma = lista[-1]
me = lista[0]
print(f'O maior valor foi {ma}')
print(f'O menor valor foi {me}')
print(lista2)
print(f'O maior valor está na posição {lista2.index(ma)})')
print(f'O menor valor está na posição {lista2.index(me)})')
