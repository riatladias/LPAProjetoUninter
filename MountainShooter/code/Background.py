#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIND_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] * 2
        if self.rect.right <= 0:
            self.rect.left = WIND_WIDTH
