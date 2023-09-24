n = int(input('Digite o numero que deseja saber se é primo: '))
s = 0
for c in range(n, 0, -1):
    print(c)
    primo = n % c
    if primo == 0:
        s = s + 1
if s == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')