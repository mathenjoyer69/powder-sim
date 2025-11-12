import pygame
import AirBlock
import StoneBlock
import SandBlock


class Button:
    def __init__(self, x, y, width, height, variable, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.original_color = color
        self.variable = variable

    def draw(self, surface):
        self.color = self.original_color if self.variable else (255, 255, 255)
        pygame.draw.rect(surface, self.color, self.rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

class Simulation:
    def __init__(self, screen, width, height, speed, matrix):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed
        self.matrix = matrix
        self.type = 1
        self.button = Button(0, 0, 40, 40, True, (120, 120, 120))
        self.button1 = Button(100, 0, 40, 40, True, (222, 186, 69))
        self.button2 = Button(200, 0, 40, 40, True, (120, 120, 120))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.update_interval = 100
        self.last_update_time = 0
        self.update_hold = 50
        self.last_update_time_hold = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= self.update_interval:
            self.last_update_time = current_time
            if self.button.variable:
                n = len(self.matrix)
                for i in range(n - 1, -1, -1):
                    for j in range(n):
                        block = self.matrix[i][j]
                        block.update(self.matrix)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        if self.button.variable:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[1])):
                    block = self.matrix[i][j]
                    block.draw(surface)
        else:
            self.button1.draw(surface)
            self.button2.draw(surface)

        self.button.draw(surface)

    def add_block(self, b_type, pos):
        if self.matrix[pos[1]][pos[0]].type == 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time_hold >= self.update_hold:
                self.last_update_time_hold = current_time
                list_x = pos[0]
                list_y = pos[1]
                if b_type == 1:
                    self.matrix[list_y][list_x] = StoneBlock.StoneBlock(list_x * 20, list_y * 20, b_type)
                if b_type == 2:
                    print(pos)
                    self.matrix[list_y][list_x] = SandBlock.SandBlock(list_x * 20, list_y * 20, b_type)

    @staticmethod
    def get_mouse_index(mouse_pos):
        return int(mouse_pos[0]/20), int(mouse_pos[1]/20)

    def run(self):
        running = True
        mouse_held = False
        while running:
            self.update()
            self.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_held = True
                        if self.button.is_over(pygame.mouse.get_pos()):
                            self.button.variable = not self.button.variable
                        if self.button.variable and not self.button.is_over(pygame.mouse.get_pos()):
                            print("Button pressed")
                            self.add_block(self.type, self.get_mouse_index(pygame.mouse.get_pos()))
                        else:
                            #sand button
                            if self.button1.is_over(pygame.mouse.get_pos()):
                                self.button.original_color = self.button1.color
                                self.type = 2
                            elif self.button2.is_over(pygame.mouse.get_pos()):
                                self.button.original_color = self.button2.color
                                self.type = 1

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        mouse_held = False

            if mouse_held and self.button.variable and not self.button.is_over(pygame.mouse.get_pos()):
                mouse_pos = pygame.mouse.get_pos()
                list_x, list_y = self.get_mouse_index(mouse_pos)
                if 0 <= list_x < len(self.matrix[0]) and 0 <= list_y < len(self.matrix):
                    self.add_block(self.type, (list_x, list_y))


            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    matrix =  [[AirBlock.AirBlock(i*20, j*20, (0, 0, 0), 0) for i in range(30)] for j in range(30)]

    sim = Simulation(screen, 600, 600, 0.1, matrix)
    sim.run()

main()
