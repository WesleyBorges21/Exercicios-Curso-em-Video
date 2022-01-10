cont = 1
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Comprasso', 9.90, 'Mochila', 120.00,
         'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print('{:^30}'.format(' Listagem de preço '))
print('-' * 30)
for c in lista:
    if cont % 2 != 0:
     print('{:.<20}R$ '.format(c),end='')
    else:
        print('{:>6.2f}'.format(c))
    cont += 1
print('-' * 30)
