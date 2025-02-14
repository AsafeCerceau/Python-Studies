# Crie um programa que faça o computador jogar Jokenpô com você

import random

while True:
    try:
        print('\nEscolha:')

        pedra = print('1 - Pedra')
        papel = print('2 - Papel')
        tesoura = print('3 - Tesoura')
        
        escolha = int(input('Resposta: '))
        
        if (escolha == '1') or (escolha == '2') or (escolha == '3'):
            bot = random.choice[pedra, papel, tesoura]
            print(bot)
        
        break
    except ValueError:
        print('Por favor, escolha uma das opções disponíveis.')