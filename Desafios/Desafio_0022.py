# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > o nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
#nome = 'André da Silva Júnior de Oliveira Santos'

upper = nome.upper()
print('Seu nome em maiúsculas fica: {}'.format(upper))

lower = nome.lower()
print('Seu nome em minúsculas fica: {}'.format(lower))

nospace = nome.replace(' ','')
leng = len(nospace)
print('Seu nome tem ao todo {} letras'.format(leng))
#ou
#aa = len("".join(split))
#print(aa)

pn = nome.split()[0]
split = nome.split()
cont_split = split[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(pn,len(cont_split)))




