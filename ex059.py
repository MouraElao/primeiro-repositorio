n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
escolha = 0
while escolha != 5:
    print('O que voce deseja fazer com os numeros que serão inseridos? ')
    print('''[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    escolha = int(input('Digite a opção escolhida: '))
    if escolha == 1:
        s = n1 + n2
        print('A soma é: {}'.format(s))
    elif escolha == 2:
        m = n1 * n2
        print('A multiplicação é: {}'.format(m))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior valor é {}'.format(maior))
        else:
            print('Os valores são iguais')
    elif escolha == 4:
        print('informe os numeros: ')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    elif escolha == 5:
        print('ACABOU')
    else:
        print('Valores digitados não aceitos, tente novamente')
    print('º-'*10)
print('Fim do programa ')

