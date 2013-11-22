import pygame
import os


class Hex(object):
    # initialization function
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        self.screen = screen

    # blit self
    def draw(self):
        return(self.screen, (self.x, self.y))


class Game(object):
    # initialization method
    def __init__(self):
        pygame.init()
        self.screen_size = self.screen_width, self.screen_height = 1280, 800
        self.screen = pygame.display.set_mode(self.screen_size)  #  , pygame.FULLSCREEN)
        self.game_over = False
        self.is_running = False
        self.newGame()
        self.clock = pygame.time.Clock()

        # hex stuff
        self.hex_list = list()
        self.hex_width = 62
        self.hex_height = 52
        self.hexagon = pygame.image.load(os.path.join('img','hex_green.png')).convert_alpha()
        self.makeGrid()
        
    # starts new game
    def newGame(self):
        self.game_over = True

    # make hex grid
    def makeGrid(self):
        for x in range(int(self.screen_width // (self.hex_width * .75))):
            for y in range(int(self.screen_height // self.hex_height)):
                ren_x = x * self.hex_width - x * self.hex_width // 4
                ren_y = y

                if x % 2:
                    ren_y = ren_y * self.hex_height + self.hex_height // 2
                else:
                    ren_y *= self.hex_height

                self.hex_list.append(Hex(self.hexagon, ren_x, ren_y))

    # draw hex grid
    def drawGrid(self):
        for myHex in self.hex_list:
            self.screen.blit(*myHex.draw())

    # main game loop
    def play(self):
        self.newGame()
        self.is_running = True

        while self.is_running:
            self.clock.tick(60)
            print(self.clock.get_fps())
            # update screen and display it
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    self.is_running = False
                    pygame.quit()
                    break
                else:
                    self.screen.fill((0,0,0))
                    self.drawGrid()

                    pygame.display.flip()
            


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
