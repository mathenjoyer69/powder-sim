import pygame

class BaseBlock:
    def __init__(self, x, y, color, type):
        self.x = x
        self.y = y
        self.size = 20
        self.color = color
        self.list_x = x // 20
        self.list_y = y // 20
        self.type = type
        self.rect = pygame.Rect(self.list_x * 20, self.list_y * 20, self.size, self.size)
