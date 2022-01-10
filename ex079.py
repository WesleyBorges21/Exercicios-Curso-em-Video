lista = []
while True:
    nun = (int(input("Digite um valor: ")))
    if nun not in lista:
        lista.append(nun)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opçao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opçao == 'N':
        break
print('-=' * 30)
lista.sort()
print(f'Você digitou os valores: {lista}')
