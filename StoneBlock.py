import pygame
import BaseBlock

class StoneBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, type):
        super().__init__(x, y, (120, 120, 120), type)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, matrix):
        pass