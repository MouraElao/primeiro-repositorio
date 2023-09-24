c = cm = cf =0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        c += 1
    sexo = str(input('Informe o sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        cm += 1
    if sexo == 'F' and idade < 20:
        cf += 1
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F]')).strip().upper()[0]
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'{c} pessoas tem mais de 18 anos.')
print(f'{cm} homens foram cadastrados.')
print(f'{cf} mulheres tem menos de 20 anos.')
