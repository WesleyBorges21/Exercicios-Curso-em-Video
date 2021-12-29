s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 and s1 == s3:
        formato = 'EQUILÁTERO'
    elif s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2 or s2 == s3 and s2 != s1:
        formato = 'ISÓSCELES'
    elif s1 != s2 and s1 != s3:
        formato = 'ESCALENO'
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(formato))
else:
    print('Os segmentos NÂO PODEM formar um triângulo!')