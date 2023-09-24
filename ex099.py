def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados. ')
    for valor in num:
        print(f'{valor}', end=' ')
        if valor > maior:
            maior = valor
    print()
    print(f'O maior valor foi {maior}')


maior(2, 4, 3, 5, 9)
