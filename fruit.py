import pygame
import random


class Fruit(pygame.sprite.Sprite):
    def __init__(self, surface_width, surface_height):
        pygame.sprite.Sprite.__init__(self)
        self.fruits = ["raspberry", "banana", "blueberry", "cherry", "pear"]
        choice = random.choice(self.fruits)
        self.image = pygame.image.load(f"images/{choice}.png")
        if choice == "blueberry":
            self.score = -2
        else:
            self.score = 1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, surface_width - self.rect.width)
        self.rect.y = 0

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def falling(self, displacement, max_height):
        if self.rect.y > max_height -50:
            self.kill()
            return -self.score
            print("Object killed")
        self.rect.y += displacement
        return 0

    def get_score(self):
        return self.score