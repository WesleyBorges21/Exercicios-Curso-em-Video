lista = ('Corintians', 'Palmeira', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
        'Coritiba', 'Ávai', 'Ponte Preta', 'Atlético GO')
print('-=' * 30)
print(f'Lista dos times do Brasileirão: {lista}')
print('-=' * 30)
print(f'Os 5 primeiros são {lista[0:5]}')
print('-=' * 30)
print(f'os 4 últimos são: {lista[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-=' * 30)
print(f'O Chapecoense está na {lista.index("Chapecoense") + 1}ª posição')
