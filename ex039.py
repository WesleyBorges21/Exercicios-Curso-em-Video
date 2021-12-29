from datetime import date
nasc = int(input('Ano do nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade < 18:
    print('Ainda falta {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format((18 - idade) + atual))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')