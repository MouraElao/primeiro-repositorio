nome = input('Nome:').upper()
media = float(input('Média: '))
situacao = ''
if media >= 7:
    situacao = 'Aprovado'
elif media >= 5 and media < 7:
    situacao = 'em recuperação'
else:
    situacao = 'Reprovado'
meno = {'Nome': nome, 'Média': media, 'Situação': situacao}
print('=' * 30)
for k, v in meno.items(): #para cada k e v em meno.items() em que k vai ser nome e media e v a resposta disso, items() pega tudo
    print(f'{k} é igual a {v}')
print('=' * 30)
