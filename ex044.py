print('=' * 10, 'Lojas BORGES', '=' * 10)
preço = float(input('Preço das compras: R$'))
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    desconto = preço - (preço * 10 / 100)
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, desconto ))
elif opçao == 2:
    desconto = preço - (preço * 5 / 100)
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, desconto))
elif opçao == 3:
    parcela = preço / 2
    print('Sua compra de R${}, vai ser dividida em 2 parcelas de R${} SEM JUROS.'.format(preço, parcela))
elif opçao == 4:
    divisao = int(input('Quantas parcelas? '))
    acrescimo = preço + (preço * 20 / 100)
    parcela = acrescimo / divisao
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(divisao, parcela))
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, acrescimo))
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
