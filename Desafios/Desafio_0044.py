# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros.

produto = input('Digite o nome do produto: ')

while True:
    try:
        preco = float(input('Informe o preço do produto: '))
        break
    except ValueError:
        print('Digite um valor válido para o preço')

while True:
    try: 
        
        print('\nEscolha a forma de pagamento: \n')

        print('1 - À vista')
        print('2 - Parcelado')

        formaPagamento = input('Reposta: ')

        if formaPagamento == '1':
            print('\nEscolha o meio de pagamento\n')
            
            print('1 - Dinheiro (10% de desconto)')
            print('2 - Cheque (10% de desconto)')
            print('3 - Cartão: (5% de desconto)')
            
            meioPagamento = input('Resposta: ')
            
            if meioPagamento =='1' or meioPagamento =='2': # Para pagamento em dinheiro ou cheque
                print(f'Preço: R${preco:.2f}')
                print(f'Preço com desconto R${preco - preco * 0.1:.2f}')
             
            elif meioPagamento =='3': # Para pagamento no cartão à vista
                print(f'Preço: R${preco:.2f}')
                print(f'Preço com desconto R${preco - preco * 0.05:.2f}')
                
            else:
                print('Por favor, digite uma opção válida\n')
                continue 
            break
        
        elif formaPagamento =='2': #Para parcelar no cartão
            print('Escolha em quantas vezes você deseja parcelar\n')
            
            print('1 - 2x (preço normal)')
            print('2 - 3x (20% de juros)')
            
            parcelas = input('Resposta: ')
            
            if parcelas =='1': # Parcelado em 2 vezes
                print(f'\nPreço do produto: R${preco:.2f}')
                print(f'Valor de cada parcela: R${preco / 2:.2f}')
                
            elif parcelas =='2': # Parcelado em 3 vezes
                print(f'Preço do produto: R${preco:.2f}')
                print(f'Valor de cada parcela: R${(preco * 0.2 + preco) / 3:.2f}')
                print(f'Valor total: R${preco * 0.2 + preco:.2f}')
                
            else: # Caso o usuário digite alguma opção que não existe
                print('Por favor, digite uma opção válida\n')
                continue 
        
        else:
            print('Por favor, digite uma opção válida')
            continue
        break
         
    except ValueError:
        print('Por favor, digite uma opção válida')
        
        
