def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show:(opcional) Mostrar ou não a conta
    :return:O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f


b = int(input('Digite o número que deseja saber o fatorial: '))
print(fatorial(b, True))
