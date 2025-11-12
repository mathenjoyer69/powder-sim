import BaseBlock
import pygame

class DirtBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, type):
        super().__init__(x, y, (101, 67, 33), type)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, matrix):
        max_y = len(matrix) - 1
        max_x = len(matrix[0]) - 1
        x = self.list_x
        y = self.list_y

        def move_to(nx, ny):
            # swaps objects in matrix because x and y are reversed in the matrix
            matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
            # updates position
            self.list_x, self.list_y = nx, ny
            self.x, self.y = nx * 20, ny * 20
            self.rect.topleft = (self.x, self.y)