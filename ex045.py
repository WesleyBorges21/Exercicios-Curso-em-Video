from random import randint
from time import sleep
computador = randint(0, 2)
print('''Suas opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opçao = int(input('Qual é a sua jogada? '))
print('jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('po!!!')
if opçao == 0:
    if computador == 0:
        print('-=' * 20)
        print('Computador jogou Pedra')
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('Empate')
    elif computador == 1:
        print('-=' * 20)
        print('Computador jogou Papel')
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('Computador Ganhou')
    elif computador == 2:
        print('-=' * 20)
        print('Computador jogou Tesoura')
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('jogador ganhou')
elif opçao == 1:
    if computador == 0:
        print('-=' * 20)
        print('Computador jogou Pedra')
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('jogador ganhou')
    elif computador == 1:
        print('-=' * 20)
        print('Computador jogou Papel')
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('Empate')
    elif computador == 2:
        print('-=' * 20)
        print('Computador jogou Tesoura')
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('Computador ganhou')
elif opçao == 2:
    if computador == 0:
        print('-=' * 20)
        print('Computador jogou Pedra')
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('Computador ganhou')
    elif computador == 1:
        print('-=' * 20)
        print('Computador jogou Papel')
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('Jogador ganhou')
    elif computador == 2:
        print('-=' * 20)
        print('Computador jogou Tesoura')
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('Empate')
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE!')
