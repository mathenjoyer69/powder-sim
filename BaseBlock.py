import pygame

class BaseBlock:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.size = 20
        self.color = color
        self.list_x = x / 20
        self.list_y = y / 20



    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.size,self.size))
        print(3)
