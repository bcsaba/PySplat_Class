import pygame

from turret import Turret


class Game:
    def __init__(self):
        self.game_over = False

        pygame.init()
        self.surface = pygame.display.set_mode([600, 600])
        pygame.display.set_caption("PySplat")
        self.surface.fill((0, 0, 0))

        self.turret = Turret(600, 600)

        self.main_loop()

    def main_loop(self):
        while self.game_over == False:
            self.turret.draw(self.surface)
            pygame.display.update()



def main():
    game = Game()


if __name__ == '__main__':
    main()
