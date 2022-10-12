import pygame

from turret import Turret


class Game:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 600
        self.game_over = False

        pygame.init()
        self.surface = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption("PySplat")
        self.surface.fill((0, 0, 0))

        self.turret = Turret(self.WIDTH, self.HEIGHT)

        self.main_loop()

    def main_loop(self):
        while self.game_over == False:
            self.turret.draw(self.surface)
            pygame.display.update()



def main():
    game = Game()


if __name__ == '__main__':
    main()
