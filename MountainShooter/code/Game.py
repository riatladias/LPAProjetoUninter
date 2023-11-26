#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIND_HEIGHT, WIND_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))

    def run(self, ):


        while True:
            menu = Menu(self.window)
            menu.run()


