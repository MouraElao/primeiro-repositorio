nome = input('Nome do Jogador:')
p = int(input('Quantas partidas ele jogou?'))
gols = list()
total = 0
for c in range(0, p):
    gols1 = (int(input(f'Quantos gols ele fez na partida {c}?')))
    gols.append(gols1)
    total = total +gols1
cad = {'Nome': nome, 'Gols': gols, 'Total': total}
print('-=' * 30)
print(cad)
print('-=' * 30)
for k, v in cad.items():
    print(f'O campo {k} tem valor {v}')
cad['Partidas'] = p
print('-=' * 30)
print(f'O jogador {cad["Nome"]} jogou {cad["Partidas"]} Partidas.')
for c in range(0, p):
    print(f' => Na Partida {c}, o jogador fez {gols[c]}')
print(f'Foi um total de {total} gols.')
