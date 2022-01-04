n = int(input('Digite um número para calcular seu fatorial: '))
c = n
fatorial = 1
while c != 0:
    fatorial = c * fatorial
    c -= 1
print('O fatorial de {} é {}'.format(n, fatorial))
