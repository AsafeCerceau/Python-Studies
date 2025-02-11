# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

while True:
    try:
        primeiroNumero = int(input('Digite um número inteiro: '))
        
        
        segundoNumero = int(input('Digite outro número inteiro: '))
        break
    
    except ValueError:
        print('Por favor, digite um número válido.\n')
        

if (primeiroNumero > segundoNumero):
        
        print(f'O primeiro valor é maior')
        
elif (segundoNumero > primeiroNumero):
        print(f'O segundo valor é maior')
        
elif (primeiroNumero == segundoNumero):
        print(f'Não existe valor maior, os são iguais.')
