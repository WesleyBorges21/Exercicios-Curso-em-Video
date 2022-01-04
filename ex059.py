from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor: '))
fim = False
while not fim:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opçao = int(input('Qual sua opção? '))
    if opçao == 5:
        fim = True
    elif opçao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {} '.format(n1, n2, soma))
    elif opçao == 2:
        multiplicaçao = n1 * n2
        print('A miltiplicação de {} x {} é {}'.format(n1, n2, multiplicaçao))
    elif opçao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maios valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente')
    print('-=' * 20)
    sleep(1)
print('Programa encerrado!')
