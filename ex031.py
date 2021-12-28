km = float(input('Qual é a distancia da sua viajem? '))
if km <= 200:
    custo = km * 0.5
    print('Você esta presta a começar um viajem de {:.1f}KM'.format(km))
    print('Eo  preço da sua passagem será de R${:.2f}'.format(custo))
else:
    custo = km * 0.45
    print('Você esta presta a começar um viajem de {:.1f}KM'.format(km))
    print('E o preço da sua passagem será de R${:.2f}'.format(custo))