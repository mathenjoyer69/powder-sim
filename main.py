import pygame
import numpy as np
import AirBlock
import StoneBlock

class Simulation:
    def __init__(self, screen, width, height, speed, matrix):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed
        self.matrix = matrix

    def update(self):
        n = len(self.matrix)
        for i in range(n, -1, -1):
            for j in range(n):
                block = self.matrix[i][j]
                block.update(self.matrix)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[1])):
                block = self.matrix[i][j]
                block.draw(surface)

    def add_block(self, type, pos):
        list_x = pos[0]
        list_y = pos[1]
        if type == 1:
            self.matrix[list_y][list_x] = StoneBlock.StoneBlock(list_x*20, list_y*20, type)

    def get_mouse_index(self, mouse_pos):
        return int(mouse_pos[0]/20), int(mouse_pos[1]/20)

    def run(self):
        running = True
        while running:
            self.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.add_block(1, self.get_mouse_index(pygame.mouse.get_pos()))
            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    matrix =  [[AirBlock.AirBlock(i*20, j*20, (0, 0, 0), 0) for i in range(40)] for j in range(40)]

    sim = Simulation(screen, 800, 800, 0.1, matrix)
    sim.run()

main()
