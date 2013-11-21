import pygame

class Game(object):
    # initialization method
    def __init__(self):
        pygame.init()
        self.screen_size = self.screen_width, screen_height = 1280, 800
        self.screen = pygame.display.set_mode(self.screen_size)  #  , pygame.FULLSCREEN)
        self.game_over = False
        self.is_running = False
        self.newGame()
        
    # starts new game
    def newGame(self):
        self.game_over = True

    # main game loop
    def play(self):
        self.newGame()
        self.is_running = True

        while self.is_running:
            # update screen and display it
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    self.is_running = False
                    pygame.quit()
                    break
                else:
                    self.screen.fill((0,0,0))
                    pygame.display.flip()
            


if __name__ == '__main__':
    my_game = Game()
    my_game.play()
