from random import randint
print('~'*20)
print('ÍMPAR OU PAR')
print('~'*20)
v = 0
while True:
    n = int(input('Digite um numero:'))
    comp = randint(0, 11)
    s = n + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR? [I/P]')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador jogou {comp}. total de {s}')
    print('Deu par' if s % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if s % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if s % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
print(f'O jogo se encerrou com o jogador com {v} vitórias.')


