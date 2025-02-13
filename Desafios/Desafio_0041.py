# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

nome = (input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

categoria = idade

if idade <= 9 and idade < 14:
    categoria = 'MIRIM'

elif idade <= 14 and idade < 19:
    categoria = 'INFANTIL'

elif idade <= 19:
    categoria = 'JUNIOR'

elif idade <= 20:
    categoria = 'SÊNIOR'
    
elif idade > 20:
    categoria = 'MASTER'    

print(f'Sua categoria é: {categoria}')
