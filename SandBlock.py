import pygame

import BaseBlock


class SandBlock(BaseBlock.BaseBlock):
    def __init__(self, x, y, type = 1):
        super().__init__(x, y, (222, 186, 69),type)
        self.temp = 20



    def update(self,matrix):
        if self.list_y < len(matrix):
            if matrix[self.list_y + 1][self.list_x] == 0:
                self.list_y += 1
                self.y += 20
            elif matrix[self.list_y + 1][self.list_x - 1] == 0:
                self.list_y += 1
                self.y += 20
                self.list_x -= 1
                self.x -= 20
            elif matrix[self.list_y + 1][self.list_x + 1] == 0:
                self.list_y += 1
                self.y += 20
                self.list_x += 1
                self.x += 20

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

