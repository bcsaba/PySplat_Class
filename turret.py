import pygame

class Turret(pygame.sprite.Sprite):
    def __init__(self, surface_width, surface_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/turret.png")
        self.rect = self.image.get_rect()
        self.rect.x = (surface_width - self.rect.width) / 2
        self.rect.y = surface_height - self.rect.height - 5

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


