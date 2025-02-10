# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo 

# Para que um triângulo seja formado, a soma de dois lados nunca pode ser menor do que o terceiro.

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('Não é possível formar um triângulo, pois a soma de dois lados é menor do que o terceiro lado.')

else:
    print('Parabéns, é possível formar um triângulo!')