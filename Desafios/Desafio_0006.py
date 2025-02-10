#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n0 = int(input('Digite um número: '))
n1 = n0 * 2
n2 = n0 * 3
n3 = n0 ** (1/2)
#n3 = pow(n0, (1/2)) #Esse é outro jeito de calcular a Raiz Quadrada

print(' O drobro de {} é {}\n O triplo é de {}\n A Raiz Quadrada é de {:.2f}'.format(n0,n1,n2,n3))

#É possível fazer tudo na mesma linha de código. Segue o exemplo abaixo:
#print(' O drobro de {} é {}\n O triplo é de {}\n A Raiz Quadrada é de {:.2f}'.format(n0,(n0*2),(n0*3),(n0**(1/2))))
