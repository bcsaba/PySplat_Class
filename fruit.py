import pygame
import random

cordx = random.randint(0, 300)

class Fruits(pygame.sprite.Sprite):
    def __init__(self, surface_width, surface_height):
        pygame.sprite.Sprite.__init__(self)
        self.banana = pygame.image.load("images/banana.png")
        self.blueberry = pygame.image.load("images/blueberry.png")
        self.cherry = pygame.image.load("images/cherry.png")
        self.pear = pygame.image.load("images/pear.png")
        self.raspberry = pygame.image.load("images/raspberry.png")
        self.strawberry = pygame.image.load("images/strawberry.png")
        self.fruits = [self.banana, self.blueberry, self.cherry, self.pear, self.raspberry, self.strawberry]
        self.rect.x = cordx
        self.rect.y = 0

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def falling(self, displacement):
        self.rect.y -= displacement