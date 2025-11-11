import pygame
import BaseBlock


class AirBlock(BaseBlock):
    def __init__(self, x, y, size, type=0):
        super().__init__(x, y, size, type)

    def update(self, matrix):
        pass

    def draw(self, surface):
        pass