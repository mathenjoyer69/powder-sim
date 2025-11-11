import pygame
import AirBlock
import BaseBlock


class SandBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, type):
        super().__init__(x, y, (222, 186, 69),type)
        self.temp = 20



    def update(self, matrix):
        max_y = len(matrix) - 1
        max_x = len(matrix[0]) - 1
        x = self.list_x
        y = self.list_y

        def move_to(nx, ny):
            # swap objects in matrix
            matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
            # update this sand block’s indices/coords/rect
            self.list_x, self.list_y = nx, ny
            self.x, self.y = nx * 20, ny * 20
            self.rect.topleft = (self.x, self.y)

        if y < max_y and matrix[y + 1][x].type == 0:
            move_to(x, y + 1)
            return matrix

            # try down-left
        if y < max_y and x > 0 and matrix[y + 1][x - 1].type == 0:
            move_to(x, y + 1)
            return matrix

            # try down-right
        if y < max_y and x < max_x and matrix[y + 1][x + 1].type == 0:
            move_to(x, y + 1)
            return matrix

        return matrix

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)

