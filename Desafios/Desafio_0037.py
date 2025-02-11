# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

while True:  # Vai manter o loop até o usuário digitar um número que seja válido
    try:
        inteiro = int(input('Digite um número inteiro: '))
        break  # Sai do loop se a execução for bem sucedida
    except ValueError:
        print('Por favor, digite apenas número inteiros.\n')

print('Agora, selecione como ele será convertido:\n')

print('1 - Converter para binário')
print('2 - Converter para octal')
print('3 - Converter para hexadecimal')

while True:
    conversao = input()

    if conversao == '1':
        binario = bin(inteiro)  # 'bin' converte automaticamente para binário
        print(f'o número {inteiro} em binário é: {binario[2:]}')
        break

    elif conversao == '2':
        octal = oct(inteiro)  # 'oct' converte automaticamente para octal
        print(f'o número {inteiro} em octal é: {octal[2:]}')
        break

    elif conversao == '3':
        # 'hex' converte automaticamente para hexadecimal
        hexadecimal = hex(inteiro)
        print(f'o número {inteiro} em hexadecimal é: {hexadecimal[2:]}')
        break

    else:
        print('Opção inválida. Por favor, digite umas das opções disponíveis.')
