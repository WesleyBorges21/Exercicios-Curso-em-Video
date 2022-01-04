idtotal = 0
hidade = 0
mvelho = ''
contf = 0
for c in range(1, 5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idtotal += idade
    if sexo == 'M':
        if idade > hidade:
            hidade = idade
            mvelho = nome
    elif sexo == 'F' and idade < 20:
        contf += 1
medidade = idtotal / 4
print('A média de idade do grupo é de {:.2f} anos'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}'.format(hidade, mvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contf))
