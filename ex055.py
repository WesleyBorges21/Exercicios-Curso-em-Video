maior = 0
menor = 9999999999
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
