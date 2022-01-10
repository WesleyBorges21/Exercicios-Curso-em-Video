from random import randint
cont = 0
print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)
computador = randint(0, 10)
while True:
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar: [P/I] ')).upper().strip()[0]
    soma = valor + computador
    if soma % 2 == 0:
        resul = 'Par'
    else:
        resul = 'Impar'
    print('-' * 40)
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} deu {resul}')
    print('-' * 40)
    if escolha != resul[0]:
        break
    cont += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    print('-=' * 20)
print(f'Game Over!!! Você venceu {cont} vezes.')
