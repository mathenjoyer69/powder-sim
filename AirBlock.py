import pygame
import BaseBlock


class AirBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, type)
        self.type = "air"

    def update(self, matrix):
        pass

    def draw(self, surface):
        pass