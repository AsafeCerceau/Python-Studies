# Escreva um programa que converta uma temperatura digitada em °C e converta em °F

C = float(input('Qual a temperatura em Celsius? '))
F = (C/5)*9 + 32
K = C+273

print('{}°C equivale a {:.1f}°F.'.format(C, F))
print('{}°C equivale a {:.1f}K'.format(C, K))
