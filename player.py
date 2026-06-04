import pygame

from bullet import Bullet
from setts import WIDTH, HEIGHT


speed = 10

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/shooter.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))
        self.delay = 3
        self.timer = self.delay

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        global speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= speed
        if self.rect.right > 890:
            self.rect.right = 890
        if self.rect.left < 0:
            self.rect.left = 0
        if keys[pygame.K_LSHIFT]:
            speed = 20
        elif not keys[pygame.K_LSHIFT]:
            speed = 10

    def shoot(self, bullet_list):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.timer <= 0:
            new_bullet = Bullet(self.rect.midtop)
            bullet_list.append(new_bullet)
            self.timer = self.delay
        self.timer -= 0.1