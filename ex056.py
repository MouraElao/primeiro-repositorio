s = 0
m = 0
sf = 0

for c in range(0, 4):
    nome = input('Qual é o seu nome? ').strip().upper()
    sexo = input('Com que sexo voce se identifica? [MASCULINO] [FEMININO]').strip().upper()
    idade = int(input('Qual é a sua idade? '))
    s += idade
    if sexo == 'MASCULINO':
        if idade > m:
            m = idade
            nomed = nome
    if sexo == 'FEMININO':
        if idade < 20:
            sf += 1
media = s / 4
print('A média de idade é: {}'.format(media))
print('A maior idade de homem é a de {} com {} anos'.format(nomed, m))
print('{} mulheres tem menos de 20 anos'.format(sf))
