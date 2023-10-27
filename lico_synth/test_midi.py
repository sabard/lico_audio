import pygame, pygame.midi

pygame.init()
pygame.midi.init()
print(pygame.midi.get_count())

pygame.midi.Input(5)

