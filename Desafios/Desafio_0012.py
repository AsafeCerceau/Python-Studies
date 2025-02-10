# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1=float(input('Qual é o preço desse produto? R$'))
d=p1*5/100
t=p1-d


print('Então com o desconto de 5%, você vai pagar R${:.2f} a menos, ou seja, ao invés de pagar R${:.2f}, o valor será de R${:.2f}'.format(d,p1,t))