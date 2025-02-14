# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

while True:
    try:
        lado1 = float(input('Digite as medidas do 1° lado do triângulo: '))
        lado2 = float(input('Digite as medidas do 2° lado do triângulo: '))
        lado3 = float(input('Digite as medidas do 3° lado do triângulo: '))

        if (lado1 + lado2 <= lado3) or (lado2 + lado3 <= lado1) or (lado1 + lado3 <= lado2):
            print(
                'Não é possível formar um triângulo com essas medidas. Por favor, faça de novo.')
            continue

        break

    except ValueError:
        print('Por favor, digite um número válido.')

if (lado1 == lado2 == lado3):
    triangulo = 'Equilátero'  # Todos os lados iguais
    motivo = 'todos os lados são iguais'

elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):  # Dois lados iguais
    triangulo = 'Isósceles'
    motivo = 'dois lados são iguais'

else:
    triangulo = 'Escaleno'  # Nenhum lado igual
    motivo = 'todos os lados são diferentes'

print(f'\nLado 1: {lado1}')
print(f'Lado 2: {lado2}')
print(f'Lado 3: {lado3}')

print(f'\nSeu Triângulo é {triangulo} porque {motivo}.')
