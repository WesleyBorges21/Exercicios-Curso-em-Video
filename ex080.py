lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
    if n > lista[-1]:
        lista.append(n)


print(lista)