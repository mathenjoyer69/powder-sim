import pygame
import BaseBlock
import AirBlock


class GlassBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, type)
        self.pressure = 0


    def update(self, matrix):
            max_y = len(matrix) - 1
            x = self.list_x
            y = self.list_y

            def move_to(nx, ny):
                # swap objects in matrix
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                # update this sand block’s indices/coords/rect
                self.list_x, self.list_y = nx, ny
                self.x, self.y = nx * 20, ny * 20
                self.rect.topleft = (self.x, self.y)

            if y < max_y and matrix[y + 1][x].type == "air":
                move_to(x, y + 1)
                return matrix
            elif matrix[y - 1][x].type == "sand" and matrix[y - 2][x].type == "sand" and matrix[y - 3][x].type == "sand":
                matrix[y][x] = AirBlock.AirBlock(self.x, self.y, (0,0,0), "air")

            return matrix
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
