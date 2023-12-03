#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIND_WIDTH, WIND_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_BLACK, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf_original = pygame.image.load('./asset/MenuBg.png')
        self.surf_resized = pygame.transform.scale(self.surf_original, size=(WIND_WIDTH, WIND_HEIGHT))

        self.rect = self.surf_resized.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:

            # Desenhar na tela
            self.window.blit(source=self.surf_resized, dest=self.rect)
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIND_WIDTH / 2), 100))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIND_WIDTH / 2), 150))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIND_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((WIND_WIDTH / 2), 300 + 30 * i))

            pygame.display.flip()

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # Testar se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # se a seta para baixo foi pressionada (+)
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # se a seta para cima foi pressionada (-)
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
