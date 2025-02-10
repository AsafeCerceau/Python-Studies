# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

lim = int(input('Digite o limite de velocidade: '))
velo = int(input('Digite a velocidade do carro: '))
multa = float(velo*7 - lim*7)


if velo > lim:
    print('Infelizmente o limite é de {}km/h, mas você estava numa velocidade de {}km/h.'.format(lim,velo))
    print('Sua multa será de R${:.2f}'.format(multa))
    
else:
    print('Você está dentro do limite de velocidade, pode passar!')
    

