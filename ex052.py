cont = 0
nun = int(input('Digite um número: '))
for c in range(1, nun + 1):
    if nun % c == 0:
        print('\33[32m{}'.format(c),  end=' ')
        cont += 1
    else:
        print('\33[31m{}'.format(c),  end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(nun, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
