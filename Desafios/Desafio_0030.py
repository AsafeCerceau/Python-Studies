# Crie um programa que leia número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import math

num = int(input('Digite um número: '))


#Pegamos o resto da divisão. Se não sobrar nada (=0), é par. Se não, é ímpar
if num % 2 == 0:
    print('O número {} é PAR.'.format(num)) 
    
else:
    print('O número {} é ÍMPAR.'.format(num))

