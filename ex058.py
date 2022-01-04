from random import randint
computador = randint(0, 10)
cont = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é seu palpite? '))
while computador != jogador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
        cont += 1
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
        cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont))
