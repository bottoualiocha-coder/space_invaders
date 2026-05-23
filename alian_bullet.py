import pygame

from setts import WIDTH, HEIGHT


class BulletAlian:
    def __init__(self, position):
        self.bullet_alian_image = pygame.Surface((5, 20))
        self.bullet_alian_image.fill("darkred")
        self.bullet_alian_rect = self.bullet_alian_image.get_rect(center= position)

    def draw(self, screen):
        screen.blit(self.bullet_alian_image, self.bullet_alian_rect)

    def move(self):
        self.bullet_alian_rect.y += 15
