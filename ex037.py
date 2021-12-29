nun = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    bin = bin(nun)
    print('{} convertido para BINÁRIO é igual a {}'.format(nun, bin[2:]))
elif opcao == 2:
    octal = oct(nun)
    print('{} convertido para OCTAL é igual a {}'.format(nun, octal[2:]))
else:
    hexa = hex(nun)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(nun, hexa[2:]))
