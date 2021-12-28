n = int(input('Me diga um número qualquer: '))
resto = n % 2
if resto == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} e ímpar'.format(n))
    