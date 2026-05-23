import pygame

from bullet import Bullet
from setts import WIDTH, HEIGHT


class Player:
    def __init__(self):
        self.image = pygame.Surface((75, 75))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))
        self.delay = 3
        self.timer = self.delay

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 10
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, bullet_list):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.timer <= 0:
            new_bullet = Bullet(self.rect.midtop)
            bullet_list.append(new_bullet)
            self.timer = self.delay
        self.timer -= 0.1