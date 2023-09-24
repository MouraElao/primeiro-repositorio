from random import randint
computador = randint(0, 10)
jogador = int(input('Escolha um numero de 0 a 10: '))
if jogador == computador:
    print('Parabéns, voce ganhou, o computador tinha escolhido {}'.format(computador))
else:
    while jogador != computador:
        print('Voce ainda não acertou, tente novamente ')
        jogador = int(input('Escolha um numero de 0 a 10:'))
print('Parabéns, voce ganhou, o computador tinha escolhido {}'.format(computador))
