produtomaismil = 0
totcompra = 0
cont = 0
prodmaisbarato = 0
nomeprodbarato = ''
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$'))
    cont += 1
    if cont == 1:
        nomeprodbarato = produto
        prodmaisbarato = valor
    totcompra += valor
    if valor > 1000:
        produtomaismil += 1
    if valor < prodmaisbarato:
        nomeprodbarato = produto
        prodmaisbarato = valor
    opçao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opçao == 'N':
        break
print(f'O total da compra foi {totcompra}')
print(f'Temos {produtomaismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeprodbarato} que custa R${prodmaisbarato}')
