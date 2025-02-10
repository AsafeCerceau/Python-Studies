# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


cidade = input('Qual cidade você mora? ')
#cidade = 'Santo André'

jooj = cidade.split()

'''
if 'SANTO' in jooj[0]:
    print('SANTO' in jooj[0])
    print('Sua cidade começa com "SANTO".')
else:
    print('SANTO' in jooj[0])
    print('Sua cidade não começa com "SANTO".')
'''

#print('SANTO' in jooj[0])

# Para deixar em maiúsculo

aba = cidade.upper().split()
print('SANTO' in aba[0])