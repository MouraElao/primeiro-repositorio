gols = list()
jogadores = list()
total = 0
while True:
    nome = input('Nome do Jogador:')
    p = int(input('Quantas partidas ele jogou?'))
    for c in range(0, p):
        gols1 = (int(input(f'Quantos gols ele fez na partida {c}?')))
        gols.append(gols1)
        total = total + gols1
        cad = {'Nome': nome, 'Gols': gols[:], 'Total': total}
    jogadores.append(cad.copy())
    gols.clear()
    total = total-total
    r = input('Quer continuar? [S/N]')
    if r not in 'SsNn':
        print('Resposta inválida, tente novamente!')
        r = input('Quer continuar? [S/N]')
    if r in 'Nn':
        break
print('-=' * 30)
print(jogadores)
print('-=' * 30)
while True:
    c = int(input('Quer ver os dados de qual jogador?'))
    for c, n in enumerate(jogadores):
        print(f'{c} {n["Nome"]} {n["Gols"]} {n["Total"]}')
        break
    r = input('Quer continuar ? [S/N]')
    if r in 'Nn':
        break

