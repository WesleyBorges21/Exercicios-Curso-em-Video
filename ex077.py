lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in lista:
    print(f'\nNa palavra {(c)} temos ', end='')
    for vogal in c:
        if vogal in 'AEIOU':
            print(f'{vogal.lower()}', end=' ')

