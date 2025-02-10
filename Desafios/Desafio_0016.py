# Crie um programa que leia um número Real qualquer pelo teclado e mostra na tela a sua posição inteira
# Exemplo:
#   Digite um número: 6.127
#   O número 6.127 tem a parte inteira 6.


# Real=float(input('Digite um número: '))
# Int = int(Real)

# print('O número {} tem a parte inteira {}'.format(Real,Int))

# ------------------------------------------------------------------

import math

Real = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}.'.format(Real, math.trunc(Real)))
#_____________________________________
#_____________________________________
#from math import trunc #Como estamos usando só um comando, não precisamos pegar a biblioteca inteira

#Real = float(input('Digite um número: '))


#print('O número {} tem a parte inteira {}'.format(Real,trunc(Real)))
