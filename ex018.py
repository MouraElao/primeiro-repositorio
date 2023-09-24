import math
angulo = float(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor de seno é {}, o de cosseno é {} e a tangente é {} desse angulo'.format(seno,cosseno,tangente))