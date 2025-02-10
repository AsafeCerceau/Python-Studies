# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$3.27

n1 = float(input('Quantos reais você tem na sua carteira? R$'))
r = float(3.27)
t = n1/r

print('Com R${:.2f}, você consegue comprar US${:.2f}.'.format(n1,t))