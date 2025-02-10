# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = int(input('Quantos Km tem sua viagem? '))
a = float(viagem * 0.5)
b = float(viagem * 0.45)

if viagem <= 200:
    print('Como sua viagem é de {}Km, a passagem custará R${:.2f}'.format(viagem,a))
    
else:
    print('Como sua viagem é de {}Km, a passagem custará R${:.2f}'.format(viagem,b))
