# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0,5)
resposta = int(input('Digite um número inteiro de 0 a 5: '))


print('O número é: {}'.format(num))

if resposta == num:
    print('Parabéns, você acertou o número!')

else:
    print('Você errou. Boa sorte na próxima vez!')