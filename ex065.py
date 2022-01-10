cont = media = soma = 0
opcao = ''
while opcao != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    soma += n
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
media = soma / cont
print('Você digitou {} números e a média foi {:.2f} '.format(cont, media))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))
