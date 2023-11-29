import pygame

clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('util/hino.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)