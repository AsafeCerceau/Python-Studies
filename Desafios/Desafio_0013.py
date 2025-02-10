# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento.

s1=float(input('Qual o seu salário atual? R$'))
nv=(s1*15/100)+s1


print('Você vai ganhar um aumento de 15%. Como seu salário atual é de R${:.2f}, então seu novo salário será de R${:.2f}.'.format(s1,nv))