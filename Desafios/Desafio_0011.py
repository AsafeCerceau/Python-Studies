# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que  cada litro de tinta pinta uma área de 2m².

#l = float(input('Qual a largura dessa parede?'))
#h = float(input('E Qual é a altura dela?'))
#a = l*h
#t = a/2

#print('Então sua parede tem {:.2f}m². Sabendo que cada litro de tinta pinta uma área de 2m², será necessário {:.2f} litros de \ntinta para pintar toda a parede'.format(a, t))

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
área = largura*altura
tinta = área / 2

print('Sua parede tem a dimensão de {}x{}. Logo, sua área é de {:.3f}m².'.format(largura,altura,área))
print('Para pintar essa parede, será necessário {:.3f} litros de tinta.'.format(tinta))