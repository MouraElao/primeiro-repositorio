def ficha(a='<DESCONHECIDO>', b=0):
    print(f'O jogador {a} fez {b} gols no campeonato.')


nome = input('Nome do jogador: ')
gols = (input('Quantos gols ele fez? '))
if gols.isnumeric(): #está verificando se a variavel 'gols' pode ser numérico
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '': #se tirando todos os espaços, ficar vazia
    ficha(b=gols)
else:
    ficha(nome, gols)

