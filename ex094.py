dados = list()
soma = media = 0
while True:
    nome = str(input('Nome:')).upper()
    sexo = input('Sexo [M/F]: ')
    if sexo not in 'MmFf':
        print('Resposta não aceita')
        sexo = input('Sexo [M/F]: ')
    idade = int(input('Idade:'))
    soma += idade
    dados1 = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    dados.append(dados1.copy())
    r = input('Quer continuar? [S/N]')
    if r not in 'SsNn':
        print('Resposta não aceita')
        r = input('Quer continuar? [S/N]')
    if r in 'Nn':
        break
print(f'Foram cadastradas {dados.__len__()} Pessoas')
media = soma/dados.__len__()
print(f'A média de idade é igual a {media:5.2f}')
listam = list()
for c in range(0, dados.__len__()):
    if dados[c]['Sexo'] == 'f':
        listam.append(dados[c]['Nome'])
for k, v in enumerate(listam):
    print(f'A {k+1}º mulher cadastrada foi a {v}')
listap = list()
for c in range(0, dados.__len__()):
    if dados[c]['Idade'] > media:
        listap.append(dados[c]['Nome'])
for k, v in enumerate(listap):
    print(f'A {k+1}º pessoa cadastrada com idade acima da média foi a(o) {v}')
