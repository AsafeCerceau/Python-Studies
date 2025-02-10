# Faça um programa queleia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

'''
if (n1>n2) and (n1>n3) and (n2<n3):
    print('Maior número: {}'.format(n1))
    print('Número meio: {}'.format(n3))
    print('Menor número: {}'.format(n2))

if (n1>n2) and (n1>n3) and (n3<n2):
    print('Maior número: {}'.format(n1))
    print('Número meio: {}'.format(n2))
    print('Menor número: {}'.format(n3))

if (n2>n1) and (n2>n3) and (n1<n3):
    print('Maior número: {}'.format(n2))
    print('Número meio: {}'.format(n3))
    print('Menor número: {}'.format(n1))
    
if (n2>n1) and (n2>n3) and (n3<n1):
    print('Maior número: {}'.format(n2))
    print('Número meio: {}'.format(n1))
    print('Menor número: {}'.format(n3))
    
if (n3>n1) and (n3>n2) and (n1<n2):
    print('Maior número: {}'.format(n3))
    print('Número meio: {}'.format(n2))
    print('Menor número: {}'.format(n1))
    
if (n3>n1) and (n3>n2) and (n2<n1):
    print('Maior número: {}'.format(n3))
    print('Número meio: {}'.format(n1))
    print('Menor número: {}'.format(n2))

'''


# De uma maneira mais simples
#Para determinar o maior número
maior = n1
if n2>maior:
    maior = n2
  
if n3>maior:
    maior = n3
    
#Para determinar o menor número
menor = n1
if n2<menor:
    menor = n2
    
if n3<menor:
    menor = n3
    
# Para determinar o número intermediário
if n1 !=maior and n1 !=menor: # Se n1 não é nem o maior nem o menor
    meio = n1 # Então n1 é o intermediário
elif n2 !=maior and n2 !=menor: # Se n2 não é nem o maior nem o menor
    meio = n2 # Então n2 é o intermediário
else:
    meio = n3 # Caso contrário, n3 é o intermediário

    
print('Maior: {}'.format(maior))
print('Meio: {}'.format(meio))
print('Menor: {}'.format(menor))
