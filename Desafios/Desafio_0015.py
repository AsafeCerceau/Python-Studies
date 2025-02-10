# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

Km = float(input('Distância percorrida em Km: '))
Dia = float(input('Dias alugados: '))
Total = (Km * 0.15) + (Dia * 60)

print('Valor Km: R${:.2f}'.format(Km*0.15))
print('Valor aluguel: R${:.2f}'.format(Dia*60))
print('Valor Total: R${:.2f}'.format(Total))
