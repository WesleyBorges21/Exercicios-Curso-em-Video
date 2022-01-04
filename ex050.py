soma = 0
cont = 0
for c in range(1, 7):
    nun = int(input('Digite {} valor: '.format(c)))
    if nun % 2 == 0:
        soma += nun
        cont += 1
print('A soma dos {} números pares é {}'.format(cont, soma))