from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que nùmero eu pensei? '))
pc = randint(0,5)
print('Processando...')
sleep(1)
if n == pc:
    print('Parabéns" Você me venceu!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(pc, n))
