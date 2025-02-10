# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o seu salário? '))

if sal > 1250:
    a = 10/100 * sal + sal
    print('Você recebera um aumento de 10%, logo seu salário irá de R${} para R${}.'.format(sal,a))

else:
    a = 15/100 * sal + sal
    print('Você recebera um aumento de 15%, logo seu salário irá de R${} para R${}.'.format(sal,a))