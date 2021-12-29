valor = float(input('Qual valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
tempo = int(input('Quantos anos de financiamento? '))
parcela = valor / (tempo * 12)
minimo = salario * 30 / 100
print('Para comprar um casa de R${:.2f} em {} anos a prestção será de R${:.2f}'.format(valor, tempo, parcela))
if parcela <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')