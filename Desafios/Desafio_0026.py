# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra: "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

'''
frase = input('Digite uma frase: ')

letra_A = (frase.count('A'))
print('A letra "A" aparece {} vez(es) nessa frase.'.format(letra_A))

primera = frase.find('A')
print('Posição que aparece a primeira vez: {}'.format(primera))

última = frase.rfind('A')
print('Posição que aparece a última vez: {}'.format(última))
'''
#print(len(frase))

# Para 'A' e 'a', transformando minúsculo em maiúsculo.

frase = str(input('Digite uma frase: ')).strip()

letra_A = frase.upper().count('A')
print('A letra "A" aparece {} vez(es) nessa frase.'.format(letra_A))

primera = frase.upper().find('A')+1
print('Posição que aparece a primeira vez: {}'.format(primera))

última = frase.upper().rfind('A')+1
print('Posição que aparece a última vez: {}'.format(última))