import pygame
import numpy as np

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

    def add_block(self, type):
         pass

    def run(self):
        running = True
        while running:
            self.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.add_block(1)
            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    matrix =  np.zeros((int(800/20), int(800/20)))
    sim = Simulation(screen, 800, 800, 0.1, matrix)
    sim.run()

main()
