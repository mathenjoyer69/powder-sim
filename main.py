import pygame
import AirBlock
import StoneBlock
import SandBlock


class Button:
    def __init__(self, x, y, width, height, variable, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.original_color = color
        self.variable = variable # this changes everytime you click the button sp u can keep track of the game state

    def draw(self, surface):
        self.color = self.original_color if self.variable else (255, 255, 255)
        pygame.draw.rect(surface, self.color, self.rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

class Simulation:
    def __init__(self, screen, matrix):
        self.screen = screen
        self.matrix = matrix
        self.type = "sand" # default block type to place
        self.buttons = [Button(0, 0, 40, 40, True, (120, 120, 120)),
                        Button(200, 0, 40, 40, True, (120, 120, 120)),
                        Button(100, 0, 40, 40, True, (222, 186, 69))
                        ]

        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.update_interval = 100 # we use this to call the update function every 100 ms without this variable the simulation would run too fast
        self.last_update_time = 0
        self.update_hold = 50 # this is used so when u hold the mouse button it doesnt place blocks too fast
        self.last_update_time_hold = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= self.update_interval: # check if 100 ms have passed and then updates the blocks
            self.last_update_time = current_time
            if self.buttons[0].variable: # only update if we are in simulation mode
                n = len(self.matrix)
                for i in range(n - 1, -1, -1): # updates the matrix from bottom to top
                    for j in range(n):
                        block = self.matrix[i][j]
                        block.update(self.matrix)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        if self.buttons[0].variable: # this variable checks if we are in the simulation mode or in the block selection mode
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[1])):
                    block = self.matrix[i][j]
                    block.draw(surface)
        else:
            for button in self.buttons[1:]: # skips the first button because he is always shown
                button.draw(surface)

        self.buttons[0].draw(surface)

    def add_block(self, b_type, pos):
        print(b_type)
        list_x = pos[0]
        list_y = pos[1]
        if b_type == 0:
            self.matrix[list_y][list_x] = AirBlock.AirBlock(list_x * 20, list_y * 20, (0, 0, 0), b_type)

        if self.matrix[pos[1]][pos[0]].type == 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time_hold >= self.update_hold:
                self.last_update_time_hold = current_time

                if b_type == 2:
                    self.matrix[list_y][list_x] = StoneBlock.StoneBlock(list_x * 20, list_y * 20, b_type)
                if b_type == 1:
                    self.matrix[list_y][list_x] = SandBlock.SandBlock(list_x * 20, list_y * 20, b_type)

    @staticmethod
    def get_mouse_index(mouse_pos):
        return int(mouse_pos[0]/20), int(mouse_pos[1]/20)

    def run(self):
        running = True
        mouse_held_l = False
        mouse_held_r = False
        while running:
            self.update()
            self.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_held_l = True
                        if self.buttons[0].is_over(pygame.mouse.get_pos()):
                            self.buttons[0].variable = not self.buttons[0].variable
                        if self.buttons[0].variable and not self.buttons[0].is_over(pygame.mouse.get_pos()):
                            self.add_block(self.type, self.get_mouse_index(pygame.mouse.get_pos()))
                        else:
                            #sand button
                            if self.buttons[1].is_over(pygame.mouse.get_pos()):
                                self.buttons[0].original_color = self.buttons[1].color
                                self.type = 2
                            elif self.buttons[2].is_over(pygame.mouse.get_pos()):
                                self.buttons[0].original_color = self.buttons[2].color
                                self.type = 1
                    if event.button == 3:
                        mouse_held_r = True
                        if self.buttons[0].variable and not self.buttons[0].is_over(pygame.mouse.get_pos()):
                            self.add_block(0, self.get_mouse_index(pygame.mouse.get_pos()))


                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        mouse_held_l = False
                    elif event.button == 3:
                        mouse_held_r = False


            if mouse_held_l and self.buttons[0].variable and not self.buttons[0].is_over(pygame.mouse.get_pos()):
                mouse_pos = pygame.mouse.get_pos()
                list_x, list_y = self.get_mouse_index(mouse_pos)
                if 0 <= list_x < len(self.matrix[0]) and 0 <= list_y < len(self.matrix):
                    self.add_block(self.type, (list_x, list_y))
            elif mouse_held_r and self.buttons[0].variable and not self.buttons[0].is_over(pygame.mouse.get_pos()):
                mouse_pos = pygame.mouse.get_pos()
                list_x, list_y = self.get_mouse_index(mouse_pos)
                if 0 <= list_x < len(self.matrix[0]) and 0 <= list_y < len(self.matrix):
                    self.add_block(0, (list_x, list_y))

            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    matrix =  [[AirBlock.AirBlock(i*20, j*20, (0, 0, 0), 0) for i in range(40)] for j in range(40)]
    sim = Simulation(screen, matrix)
    sim.run()

main()
