# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex:
#Digite um número: 1834

#unidade: 4
#dezena: 3
#Centena: 8
#Milhar: 1


#número = input('Digite um número: ')
#número = '1234'

#como string
'''
a = número
unidade = a[3]
dezena = a[2]
centena = a[1]
milhar = a[0]

print('Número: {}'.format(a))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
'''
#como forma numérica

num = int(input('Digite um número: '))

u = num // 1 % 10
print('Unidade: {}'.format(u))

d = num // 10 % 10
print('Dezena: {}'.format(d))

c = num // 100 % 10
print('Centena: {}'.format(c))

m = num // 1000 % 10
print('Milhar: {}'.format(m))

