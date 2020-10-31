import pygame
pygame.init()
time = int(input())

song = pygame.mixer.Sound('komon.mp3')
clock = pygame.time.Clock()
song.play(time)



while True:
    clock.tick(time)
pygame.quit()