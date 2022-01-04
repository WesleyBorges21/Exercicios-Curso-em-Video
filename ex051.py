print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
total = razao * 10 + termo
for c in range(termo, total, razao):
    print(c, ' - ', end=' ')
print('Acabou!')