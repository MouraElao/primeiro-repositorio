from random import randint
itens = ('','PEDRA', 'PAPEL', 'TESOURA')
print('tamanho', len(itens))
print('{} JOKENPO {}'.format('-'*9, '-'*9))
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
resposta = int(input('SUA JOGADA É: '))
respostac = randint(1, 3)
if resposta == respostac:
    print('EMPATE\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 1 and respostac == 2:
    print('VOCE PERDEU\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 2 and respostac == 1:
    print('VOCE GANHOU\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 1 and respostac == 3:
    print('VOCE GANHOU\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 3 and respostac == 1:
    print('VOCE PERDEU\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 2 and respostac == 3:
    print('VOCE PERDEU\nO computador escolheu {}'.format(itens[respostac]))
elif resposta == 3 and respostac == 2:
    print('VOCE GANHOU\nO computador escolheu {}'.format(itens[respostac]))


