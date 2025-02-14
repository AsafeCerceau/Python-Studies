# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

while True:
    try:
        altura = int(input('Digite sua altura (cm): '))
        peso = float(input('Digite seu peso (kg): '))

        break
    except ValueError:
        print('Por favor, digite um número válido.\n')

altura = altura / 100  # Conversão de centímetros para metros
imc = (peso / altura**2)

if (imc < 18.5):
    status = 'Abaixo do Peso'

elif (18.5 <= imc < 25):
    status = 'Peso ideal'

elif (25 <= imc < 30):
    status = 'Sobrepeso'

elif (30 <= imc <= 40):
    status = 'Obesidade'

elif (40 < imc):
    status = 'Obesidade Mórbida'

print(f'Sua altura: {altura}m.')
print(f'Seu peso: {peso:.1f}kg.')

print(f'\nSeu IMC: {imc:.2f}')
print(f'Você está em {status}')
