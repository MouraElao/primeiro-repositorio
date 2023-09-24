from random import randint
from time import sleep
jogos = list()
v = list()
ms = list()
print('-=' * 30)
print('                    JOGA NA MEGA SENA')
print('-=' * 30)
ns = int(input('Quantos jogos você quer sortear? '))
for c in range(0, ns):
    for c1 in range(0, 6):
        n = randint(0, 60)
        if n in ms:
            n = randint(0, 60)
        ms.append(n)
        ms.sort()
    jogos.append(ms[:]) #[:]copia de ms
    ms.clear() #limpa a lista para o próximo loop, dessa forma acrescenta sem o sorteio anterior (muito importante)
print('-=' * 3, f' SORTEANDO {ns} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f' Jogo {i + 1}: {l}')
    #sleep(1)
print('-=' * 5, ' BOA SORTE ', '-=' * 5)
for c2 in range(0, 6):
    n1 = randint(0, 60)
    if n1 in v:
        n1 = randint(0, 60)
    v.append(n1)
print(f'Os números vencedores foram: {v}')
s1 = 0
for c in range(0, jogos.__len__()):
    if jogos[c] == v:
        s1 = s1+1
if s1 > 0:
    print('Você ganhou!')
else:
    print('Você perdeu!')
