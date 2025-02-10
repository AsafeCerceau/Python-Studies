# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#algumas bibliotecas para isso: 'pygame', 'pydub', 'playsound'.

import pygame

#inicializar o player de música
pygame.mixer.init()

#carregar o arquivo mp3
pygame.mixer.music.load('Desafios\ex021_2.mp3') # pylint: disable=JOJ


#Reproduzir o arquivo
pygame.mixer_music.play()


#Manter o Script rodando até que a música pare
while pygame.mixer.music.get_busy(): # mantém o script em execução enquanto a música está tocando.
    pygame.time.Clock().tick(10)     # adiciona uma pequena espera no loop para evitar o uso excessivo de CPU.

#OU

#pygame.event.wait()

'''
___________________________________________________
#import playsound

# Reproduzir o arquivo MP3
#playsound.playsound("Franchesco.mp3")
'''

'''
___________________________________________________
#from pydub import AudioSegment
#from pydub.playback import play

# Carregar o arquivo MP3
#song = AudioSegment.from_mp3("Franchesco.mp3")

# Reproduzir o arquivo MP3
#play(song)
'''
