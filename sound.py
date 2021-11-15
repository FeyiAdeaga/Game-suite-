import pygame
from pygame import mixer


def music():
    pygame.init()
    pygame.mixer.music.load('POL-autumn-leaves-short.wav')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
