from math import sqrt
cto = float(input('Comprimento cateto oposto: '))
cta = float(input('Comprimento cateto adjacente: '))
hip = sqrt((cto ** 2) + (cta ** 2))
print('A hipotnusa vai medir {:.2f}'.format(hip))
