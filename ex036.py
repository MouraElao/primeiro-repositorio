vc = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o seu sálario?'))
anos = float(input('Em quantos anos você irá pagar?'))
meses = anos*12
prest = vc/meses
porcs = (salario*30)/100
print('O valor da prestação é {:.2f} reais'.format(prest))
print('30% do seu sálario é: {}'.format(porcs))
if prest > porcs:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO AUTORIZADO')
