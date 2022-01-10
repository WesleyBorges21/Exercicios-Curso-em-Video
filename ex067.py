cont = 1
while True:
    print('-' * 40)
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tabu < 0:
        break
    while cont < 11:
        resultado = tabu * cont
        print(f'{tabu} x {cont} = {resultado}')
        cont += 1
    cont = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
