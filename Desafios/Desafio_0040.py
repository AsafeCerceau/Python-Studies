# Crie um programa que leia notas de um aluno, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

notaAluno = float(input('Nota do Aluno: '))

if 0 < notaAluno < 5.0:
    print('REPROVADO')
    
elif 5 <= notaAluno <= 6.9:
    print('RECUPERAÇÃO')
    
elif 10 > notaAluno >= 7.0:
    print('APROVADO')
    
else:
    print('NOTA INVÁLIDA.')