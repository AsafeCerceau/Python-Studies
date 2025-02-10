# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

c1 = float(input('Cateto 1: '))
c2 = float(input('Cateto 2: '))
hq = pow(c1,2) + pow(c2,2)
h = math.sqrt(hq)

#print('Hipotenusa = {:.2f}'.format(h))

print('Hipotenusa = {:.2f}'.format(math.hypot(c1,c2)))