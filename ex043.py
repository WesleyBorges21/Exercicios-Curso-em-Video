peso = float(input('Qual é o seu peso: (Kg) '))
altura = float(input('Qual é a sua altura: (m) '))
imc = peso / (altura * altura)
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
