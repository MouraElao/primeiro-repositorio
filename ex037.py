n1 = int(input('Digite um numero inteiro:'))
print('Qual será a base de conversão?')
base = int(input('[1] BINÁRIO [1] --- [2] OCTAL [2] --- [3] HEXADECIMAL [3]\n'))
if base == 1:
    print('Em binário esse numero fica: {}'.format(bin(n1)[2:]))
elif base == 2:
    print('Em octal esse numero fica: {}'.format(oct(n1)[2:]))
elif base == 3:
    print('Em hexadecimal esse numero fica: {}'.format(hex(n1)[2:]))
else:
    print('Opção invalida')

