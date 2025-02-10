# Faça um programa que leia um ano qualquer se mostre se ele é Bissexto.

ano = int(input('Digite um ano: '))


#Se o resto da divisão num/4 for igual a 0 E se é verdade o resultado da divisão num/100 (!=) OU se o resto da divisão ano/400 for igual a zero.
if (ano % 4 == 0 and ano %100 !=0) or (ano % 400 ==0): #Verifica se o ano é divisível por 4 e não é divisível por 100. Se essa condição for verdadeira, o ano é bissexto. OU Se o ano for divisível por 400, ele também é bissexto, independentemente das outras condições.
    print('O ano {} é bissexto'.format(ano))
    
else:
    print('O ano {} não é bissexto.'.format(ano))   