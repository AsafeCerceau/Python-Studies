# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print ('Olá, seja bem vindo(a)! Gostaria de fazer um empréstimo?')

print('1 - SIM')
print('2 - NÃO')

resposta = input()

#Validação da resposta.
while resposta not in ['1', '2']:
    print("Opção inválida. Por favor, digite '1' para SIM ou '2' para NÃO.")
    resposta = input()

if resposta == '1':
    print('Certo! Para isso, responda as perguntas a seguir.')
    
    while True:
        try: 
            #Solicitando os valores
            valorCasa = float(input('Qual é o valor da casa? \n'))
            break
        except ValueError:
            print('Por favor, digite um valor válido.\n')
            
    while True:
        try:
            valorSalario = float(input('Qual é o seu salário? \n'))
            break
        except ValueError:
            print('Por favor, digite um valor válido.\n')
            
    while True:
        try:
            anos = int(input('Em quantos anos você vai pagar? \n'))
            break
        except ValueError:
            print('Por favor, digite um valor válido.\n')
            
    print('\nConfira as informações:\n')
    print('Valor do casa: R${}'.format(valorCasa))
    print('Salário: R${}'.format(valorSalario))
    print('Anos em que será pago: {}'.format(anos))
    
    print('\nDeseja editar algum valor? ')
    
    print('1 - SIM')
    print('2 - NÃO')
    
    respostaEdicao = input()
    
    if respostaEdicao == "1":
        
        print('\nEscolha o que deseja editar:')
        
        print('1 - Valor da Casa')
        print('2 - Salário')
        print('3 - Prazo de Pagamento')
        
        escolhaEdicao = input()
        
        if escolhaEdicao == "1":
            try:
                valorCasa = float(input('Insira o novo valor da casa: '))
            except ValueError:
                print('Por favor, digite um número válido')
        
        elif escolhaEdicao == "2":
            try:
                valorSalario = float(input('Insira o novo Salário: '))
            except ValueError:
                print('Por favor, digite um número válido.')
        
        elif escolhaEdicao == "3":
            try:
                anos = int(input('Insira o novo prazo de pagamento: '))
            except ValueError:
                    print('Por favor, digite um número válido')
        
    if respostaEdicao == '2':
        print('Certo, então vamos prosseguir.')
        print('Para isso, o valor financiado não pode exceder 30% de seu salário\n')
        
        parcelas = int (anos * 12)
        print('Salário: {}'.format(valorSalario))
        print('Valor da casa: {}'.format(valorCasa))
        print('Meses para pagar: {}\n'.format(parcelas))
        
        valorParcela = (valorCasa / parcelas)
        limiteFinanciado = (valorSalario * 0.3)
        
        print('Valor da Parcela: R${}'.format(valorParcela))
        print('Limite para sua renda: R${}\n'.format(limiteFinanciado))
        
        if valorParcela > limiteFinanciado:
            print('Infelizmente não será possível realizar um financiamento, pois a parcela excede mais de 30% de sua renda.')
            
        else:
            print('O valor do seu financiamento será de R${} por mês durante {} meses'.format(valorParcela, parcelas))
            

if resposta == '2':
    
    print('Certo, obrigado e tenha um bom dia!')