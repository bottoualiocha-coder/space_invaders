import pygame

from setts import WIDTH, HEIGHT


class BulletAlian:
    def __init__(self, position):
        self.bullet_alien_image = pygame.Surface((5, 20))
        self.bullet_alien_image.fill("darkred")
        self.bullet_alien_rect = self.bullet_alien_image.get_rect(center= position)

    def draw(self, screen):
        screen.blit(self.bullet_alien_image, self.bullet_alien_rect)

    def move(self):
        self.bullet_alien_rect.y += 15

