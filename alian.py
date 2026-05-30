import pygame
from alian_bullet import BulletAlian
from setts import WIDTH


class Alian:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.delay = 3
        self.timer = self.delay
        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_list):
        bullet_list.append(BulletAlian(self.rect.center))

    def move(self,direction):
        self.rect.x += direction * self.speed

    def need_to_turn(self):
        if self.rect.right > WIDTH or self.rect.left < 0:
            return True
        return False