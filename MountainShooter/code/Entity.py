#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import WIND_HEIGHT, WIND_WIDTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf_original = pygame.image.load('./asset/' + name + '.png')
        self.surf = pygame.transform.scale(self.surf_original, (WIND_WIDTH, WIND_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
