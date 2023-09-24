tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')), int(input('Digite um número: ')))
print(tupla)
print(f'O número 9 aparece {tupla.count(9)} vez(es)')
if tupla.count(3) > 0:
    print(f'O número 3 aparece na {tupla.index(3)+1}º posição')
else:
    print('O número 3 não aparece em nenhuma posição.')
print('Os númeres pares foram: ')
for a in tupla:
    if a % 2 == 0:
        print(a)
        