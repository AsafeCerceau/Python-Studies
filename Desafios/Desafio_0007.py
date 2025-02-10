# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média;.

n1 = float(input('Quanto Carlos tirou na primeira prova de Matemática? '))
n2 = float(input('E na segunda prova? '))
s = (n1 + n2) / 2

print('Se Carlos tirou {} na primeira prova e {} na segunda, então a média dele é de {:.1f}'.format(n1,n2,s))