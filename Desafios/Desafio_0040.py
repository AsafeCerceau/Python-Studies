# Crie um programa que leia notas de um aluno, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

while True:
    try:
        nota1 = float(input('Primeira nota: '))
        if nota1 < 0 or nota1 > 10:
            print('Por favor, escreva de 0 a 10')
            continue

        nota2 = float(input('Segunda nota: '))
        if nota2 < 0 or nota2 > 10:
            print('Por favor, escreva de 0 a 10')
            continue
        
        break
        
    except ValueError:
        print('Digite um valor válido')
 
notaAluno = (nota1 + nota2) / 2

print(f'Sua nota: {notaAluno}')

if 0 < notaAluno < 5.0:
    print('REPROVADO')

elif 5 <= notaAluno <= 6.9:
    print('RECUPERAÇÃO')

elif 10 > notaAluno >= 7.0:
    print('APROVADO')

else:
    print('NOTA INVÁLIDA.')
