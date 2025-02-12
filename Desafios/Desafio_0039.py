# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou a hora do tempo de alistamento
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

import datetime
import calendar #Para verificar os dias de cada mês (Tem meses mais curtos que outros)


print('Digite sua data de nascimento\n')
 
while True:
    try:
        
        #Para solicitar o ano de nascimento
        while True:
            ano = int(input('Ano: '))
            anoAtual = datetime.date.today().year
        
            if anoAtual >= ano >= 1900:
                break
            print('Por favor, digite de 1901 até o ano atual.')
                

        #Para solicitar o mês de nascimento
        while True:
            mes = int(input('Mês: '))
            
            if 1 <= mes <= 12:
                break    
            print('Digite de 1 a 12')
                

        #Para solicitar o dia de nascimento
        while True:
            dia = int(input('Dia: '))
            ultimoDiaMes = calendar.monthrange(ano, mes) [1] #Obtém o número correto de cada mês
            
            if 1 <= dia <= ultimoDiaMes:
                break
            print(f'Dia inválido. O {mes}° mês tem {ultimoDiaMes} dias.')
            
        break

    except ValueError:
        print('Por favor, digite um número válido.')

#Para calcular a idade
hoje = datetime.date.today()
dataNascimento = datetime.date (ano, mes, dia)
idade = (hoje.year - dataNascimento.year)

if (hoje.month, hoje.day) < (dataNascimento.month, dataNascimento.day): # Caso a pessoa ainda não tenha feito aniversário esse ano
    idade -= 1
    
print(f'\nHoje é {hoje}')
print(f'\nVocê tem {idade} anos.')

if idade < 18:
    print(f'Você ainda não tem 18 anos. Volte para se alistar em {18 - idade} anos.')

elif idade == 18:
    print(f'Está na hora de você se alistar')
    
elif idade > 18:
    print(f'Já passou {idade - 18} anos da sua hora de se alistar, tá esperando o quê?')
    
