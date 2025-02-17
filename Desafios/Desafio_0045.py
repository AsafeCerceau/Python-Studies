# Crie um programa que faça o computador jogar Jokenpô com você

import random

while True:
    try:
        print('\nEscolha:')

        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        
        escolha = int(input('Resposta: '))
         
        if escolha in [1, 2, 3]: # Isso está aqui dentro do while porque se fizer fora, a escolha vai será feita em strings, mas aqui nós queremos ela como int
            break
        else:
            print('Por favor, escolhe entre 1 e 3.')
            
    except ValueError:
        print('Por favor, escolha uma das opções disponíveis.')       
        

opcoes = ['Pedra', 'Papel', 'Tesoura']
bot = random.choice(opcoes) #random.choise retorna um valor // random.choises retorna um lista

#print (bot) #Para verificar se a escolha do bot está dando certo

if escolha ==1:
    jogador = 'Pedra'
    
elif escolha ==2:
    jogador = 'Papel'
    
elif escolha ==3:
    jogador = 'Tesoura'
    
    
print(f'\nEscolha do Jogador: {jogador}')
print(f'Escolha do bot {bot}')

if jogador == bot:
    print('\nEmpate')
    
elif (jogador == 'Pedra' and bot == 'Papel') or (jogador == 'Papel' and bot == 'Tesoura') or (jogador == 'Tesoura' and bot == 'Pedra'):
    print('Você perdeu.')
        
else:
    print('Você venceu.')
        
        
