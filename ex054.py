from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas menores de idade.'.format(menor))
print('E também tivemos {} pessoas maiores de idade.'.format(maior))
