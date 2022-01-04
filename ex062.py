p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = p1
cont = 0
fim = False
tot = 0
while not fim:
    while cont < 10 + tot:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    opcao = int(input('\nQuantos termos você quer mostrar a mais? '))
    tot += opcao
    if opcao == 0:
        fim = True
print('Progressão finalizada com {} tremos mostrados.'.format(cont))

