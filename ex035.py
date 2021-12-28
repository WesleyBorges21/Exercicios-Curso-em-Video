print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
