n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('O aluna está REPROVADO.')
elif 5 <= media < 7:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
