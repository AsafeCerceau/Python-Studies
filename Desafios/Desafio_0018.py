# Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo.

#import math
'''
cateto1 = float(input('Digite o cateto 1: '))
cateto2 = float(input('Digite o cateto2: '))
ângulo = float(input('Digite o valor do ângulo: '))
hipoq = pow(cateto1,2) + pow(cateto2,2)
hipotenusa = math.sqrt(hipoq)
seno = cateto2/hipotenusa
coseno = cateto1/hipotenusa
tangente = cateto2/cateto1

print('-' * 15)
print('Cateto Adjascente: {}'.format(cateto1))
print('Cateto Oposto: {}'.format(cateto2))
print('hipotenusa: {:.2f}'.format(hipotenusa))
print('Ângulo: {}'.format(ângulo))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(coseno))
print('Tangente: {:.2f}'.format(tangente))
'''

'''
ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
consseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))


print('Seno: {:.2f}'.format(seno))
print('Cossedo: {:.2f}'.format(consseno))
print('Tangente: {:.2f}'.format(tangente))
'''


from math import radians, sin, cos, tan

ângulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

print('O Seno de {} é {:.2f}'.format(ângulo, seno))
print('O Cosseno de {} é {:.2f}'.format(ângulo, cosseno))
print('A Tangente de {} é {:.2f}'.format(ângulo, tangente))
