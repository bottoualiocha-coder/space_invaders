import pygame
from alian_bullet import BulletAlian
from setts import WIDTH


class Alian:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/alien.png")
        self.image = pygame.transform.rotozoom(self.image, 0,1.5)
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

    def change(self):
        self.speed += 0.1
        self.rect.y += 3