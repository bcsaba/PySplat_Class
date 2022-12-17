import pygame

from turret import Turret
from fruit import Fruit
from bullet import Bullet

class Game:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 600
        self.FRUIT_DISPLACEMENT = 5
        self.game_over = False
        self.FPS = 30
        self.FRUIT_DELAY = 25
        self.loop_count = 0
        self.turretspeed = 10
        self.bulletspeed = 10
        self.score = 0

        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption("PySplat")
        self.surface.fill((0, 0, 0))

        self.turret = Turret(self.WIDTH, self.HEIGHT)
        self.fruits = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.scoreFont = pygame.font.Font("images/256BYTES.ttf", 32)
        self.main_loop()

    def main_loop(self):
        while self.game_over == False:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.game_over = True
            if pygame.key.get_pressed()[pygame.K_a]:
                self.turret.move_left(self.turretspeed)
            if pygame.key.get_pressed()[pygame.K_d]:
                self.turret.move_right(self.turretspeed, self.WIDTH)
            for evt in pygame.event.get(pygame.KEYDOWN):
                if evt.key == pygame.K_SPACE:
                    self.bullets.add(Bullet(self.HEIGHT, self.turret))
            print(self.score)

            for evt in pygame.event.get(pygame.QUIT):
                self.game_over = True

            if self.loop_count % self.FRUIT_DELAY == 0:
                self.fruits.add(Fruit(self.WIDTH, self.HEIGHT))

            self.surface.fill((0, 0, 0))
            self.turret.draw(self.surface)
            for bullet in self.bullets:
                bullet.draw(self.surface)
                bullet.update_position(self.bulletspeed)
            for fruit in self.fruits:
                fruit.draw(self.surface)
                self.score += fruit.falling(self.FRUIT_DISPLACEMENT, self.HEIGHT)

            score_text = self.scoreFont.render(f"Score: {self.score}", True, [0, 255, 0])
            self.surface.blit(score_text, (10, 10))
            pygame.display.update()

            hit_fruits = pygame.sprite.groupcollide(self.fruits, self.bullets, False, True)
            for kill in hit_fruits:
                kill.kill()
                print("object killed by player")
                self.score += kill.get_score()
                if self.score == 10:
                    self.turretspeed = 9
                    self.FRUIT_DELAY = 22
                    self.FRUIT_DISPLACEMENT = 7

                if self.score == 20:
                    self.turretspeed = 8
                    self.FRUIT_DELAY = 20
                    self.FRUIT_DISPLACEMENT = 8

                if self.score == 30:
                    self.turretspeed = 8
                    self.FRUIT_DELAY = 17
                    self.FRUIT_DISPLACEMENT = 9

                if self.score == 40:
                    self.turretspeed = 9
                    self.FRUIT_DELAY = 15
                    self.FRUIT_DISPLACEMENT = 10

            if self.score == -5:
                break





            self.clock.tick(self.FPS)
            self.loop_count += 1


def main():
    game = Game()


if __name__ == '__main__':
    main()
