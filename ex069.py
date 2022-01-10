homem = mulhermais20 = totmais18 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 20:
        totmais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade >= 20:
        mulhermais20 += 1
    print('-' * 30)
    opçao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opçao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulhermais20} mulheres com mais de 20 anos')
