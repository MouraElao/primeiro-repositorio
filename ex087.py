m = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
nl = list()
s = st = ma = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
        nl.append(m[l][c])
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    print()
for c in range(0, 9):
    if nl[c] % 2 == 0:
        s = s + nl[c]
for c in range(2, 9, 3):
    st = st + nl[c]
for c in range(3, 6):
    if nl[c] > ma:
        ma = nl[c]
print(f'A soma dos números pares é igual a: {s}')
print(f'A soma dos números da terceira coluna é igual a: {st}')
print(f'O maior valor da segunda linha é o: {ma}')
