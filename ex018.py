from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {} tem o SENO: {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO: {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a Tangente: {:.2f}'.format(ang, tan))
