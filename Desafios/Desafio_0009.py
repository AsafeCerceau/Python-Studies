# Faça um programa que leia um número Inteiro qualquer e mostre a sua tabuada.

#n = int(input('Digite um número: '))
#n0 = n * 0
#n1 = n * 1
#n2 = n * 2
#n3 = n * 3
#n4 = n * 4
#n5 = n * 5
#n6 = n * 6
#n7 = n * 7
#n8 = n * 8
#n9 = n * 9
#n10 = n * 10

#print('--------------------\n {0} * 0 = {1}\n {0} * 1 = {2}\n {0} * 2 = {3}\n {0} * 3 = {4}\n {0} * 4 = {5}\n {0} * 5 = {6}\n {0} * 6 = {7}\n {0} * 7 = {8}\n {0} * 8 = {9}\n {0} * 9 = {10}\n {0} * 10 = {11}\n--------------------'.format(n, n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

num=int(input('Digite um número para aparecer a tabuada: '))

print('-' * 15)
print('{} x {:2} = {}'.format(num, 0, num*0))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 15)