# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
alunos = [n1,n2,n3,n4]

random.shuffle(alunos)


print('Ordem do sorteio: ')
print(alunos)

#Para numerar a ordem:

#for i, ordem in enumerate(alunos,start=1):
#    print(f'{i}: {ordem}')

    