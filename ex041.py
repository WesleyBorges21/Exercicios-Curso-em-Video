from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    faixa = 'MIRIM'
elif 9 > idade <= 14:
    faixa = 'INFANTIL'
elif 14 > idade <= 19:
    faixa = 'JÚNIOR'
elif 19 > idade <= 25:
    faixa = 'SÊNIOR'
else:
    faixa = 'MASTER'
print('Classificação: {}'.format(faixa))