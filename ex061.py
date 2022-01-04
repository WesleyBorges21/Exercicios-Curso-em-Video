print('Gerador de PA')
print('-=' * 20)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    print('{} - '.format(p1), end='')
    cont += 1
    p1 = p1 + razao
print('FIM')
