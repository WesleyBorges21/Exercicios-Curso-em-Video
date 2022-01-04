valor = int(input('Digite um valor para ver sua tabuada: '))
for c in range(1, 11):
    multi = valor * c
    print('{} x {:2}= {}'.format(valor, c, multi))
