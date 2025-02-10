# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

# n0 = float(input('Qual a sua altura? '))
# n1 = n0*100
# n2 = n1*10

# print(' Então a sua altura em metros é de {}\n Em centímetros: {}\n Em milímetros: {}'.format(n0,n1,n2))

n0 = float(input('Qual a distância dessa pista em metros? '))
km = n0*0.001
hm = n0*0.01
dam = n0*0.1
dm = n0*10
cm = n0*100
mm = n0*1000

print('Dado a distância de {0} metro(s), segue: \n{1}km \n{2}hm \n{3:.1f}dam \n{4:.0f}dm \n{5:.0f}cm \n{6:.0f}mm'.format(n0,km,hm,dam,dm,cm,mm))