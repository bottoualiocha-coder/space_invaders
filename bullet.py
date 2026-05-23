import pygame


class Bullet:
    def __init__(self, position):
        self.image = pygame.Surface((5, 20))
        self.image.fill("antiquewhite")
        self.rect = self.image.get_rect(midbottom=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= 30
