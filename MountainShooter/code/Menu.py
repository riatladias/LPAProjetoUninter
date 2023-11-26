#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIND_WIDTH, WIND_HEIGHT


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf_original = pygame.image.load('./asset/MenuBg.png')
        self.surf_resized = pygame.transform.scale(self.surf_original, size=(WIND_WIDTH, WIND_HEIGHT))

        self.rect = self.surf_resized.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf_resized, dest=self.rect)
            self.menu_text(50, 'Mountain', (255, 28, 0), ((WIND_WIDTH / 2), 80))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
