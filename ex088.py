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
    sleep(0.5)
print('-=' * 5, ' BOA SORTE ', '-=' * 5)
