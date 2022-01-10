lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posiçoes ', end='')
for c, p in enumerate(lista):
    if p == maior:
        print(f'{c}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posiçoes ', end='')
for c, p in enumerate(lista):
    if p == menor:
        print(f'{c}... ', end='')
