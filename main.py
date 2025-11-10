import pygame
import numpy as np

class Simulation:
    def __init__(self, screen, width, height, speed, matrix):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))

    def run(self):
        running = True
        while running:
            self.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    matrix =  np.zeros((int(800/20), int(800/20)))
    sim = Simulation(screen, 800, 800, 0.1, matrix)
    sim.run()

main()
