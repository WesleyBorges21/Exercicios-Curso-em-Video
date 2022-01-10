print('{:-^30}'.format(' WESLEY BORGES '))
# centralizado em 30 espaços

print('{:-<30}'.format(' WESLEY BORGES '))
# alinhado a esquerda em 30 espaços

print('{:->30}'.format(' WESLEY BORGES '))
# alinhado a direita em 30 espaços

lanches = ('coca', 'batata', 'torta', 'pizza' )
print(f'A posiçao da pizza e: {lanches.index("pizza")+1}')
# index acha posição dentro da tupla

numeros = (1, 3, 5, 8, 4 )
print(f'O maior: {max(numeros)}')
print(f'O menor: {min(numeros)}')
# max pega o maior dentro da tupla e o min pega o menor