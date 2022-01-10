from random import randint
cont = maior = menor = 0
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in sorteio:
    print(c,end=' ')
    cont += 1
    if cont == 1:
        menor = c
        maior = c
    if c < menor:
        menor = c
    if c > maior:
        maior = c
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
