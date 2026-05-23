import pygame
from alian_bullet import BulletAlian


class Alian:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.delay = 3
        self.timer = self.delay

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_list):
        bullet_list.append(BulletAlian())