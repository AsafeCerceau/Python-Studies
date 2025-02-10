# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Sousa
# Primeiro: Ana
# Úiltimo: Sousa

nome = input('Escreva seu nome: ').strip()
#nome = 'Ana Maria de Sousa'

pri = nome.split()[0] # Números positivos representam a partir do primeiro elemento (0 sempre é o primeiro).
print('Primeiro: {}'.format(pri))

ult = nome.split()[-1] # Números negativos representam a partir do último elemento.
print('Último: {}'.format(ult))