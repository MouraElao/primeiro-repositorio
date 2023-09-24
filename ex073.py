tabela = ('SÃO PAULO', 'GRÊMIO', 'CRUZEIRO', 'PALMEIRAS', 'FLAMENGO',
          'INTERNACIONAL', 'BOTAFOGO', 'GOIÁS', 'CORITIBA', 'EC VITÓRIA',
          'SPORT RECIFE', 'ATLÉTICO-MG', 'ATHLETICO-PR', 'FLUMINENSE',
          'SANTOS', 'NÁUTICO', 'FIGUEIRENSE', 'VASCO DA GAMA', 'PORTUGUESA',
          'IPATINGA')
print(f'Os 5 primeiros times são {tabela[0:5]}')
print(f'Os 4 últimos colocados são {tabela[-4:]}')
print(f'Os times em ordem alfabética {sorted(tabela)}')
print(f'O {tabela[13]} estã na posição {tabela.index("FLUMINENSE")+1}')
