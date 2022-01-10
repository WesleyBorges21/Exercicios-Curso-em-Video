lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    opçao = int(input('Digite um número entre 0 e 20: '))
    if 0 <= opçao <= 20:
        break
    else:
        print('Tente novamente. ', end='')
print(f'Você digitou o número {lista[opçao]}')
