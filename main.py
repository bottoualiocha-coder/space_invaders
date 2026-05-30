import pygame
from alian import Alian
from player import Player
from random import choice

from setts import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

alien_list = []
alien_direction = 1
bullet_list = []
alien_bullet_list = []
for y in range(4):
    for x in range(8):
        alien_list.append(Alian(40 + x * 70, 100 + y * 100))

ALIAN_SHOOT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIAN_SHOOT, 2000)

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == ALIAN_SHOOT:
            choose_alian = choice(alien_list)
            choose_alian.shoot(alien_bullet_list)

    screen.fill("black")

    for alien in alien_list:
        alien.draw(screen)
        alien.move(alien_direction)
    player.draw(screen)
    player.move()
    player.shoot(bullet_list)

    for bullet in bullet_list:
        bullet.draw(screen)
        bullet.move()
        alian_index = bullet.rect.collidelist(alien_list)
        if alian_index != -1:
            alien_list.pop(alian_index)
            bullet_list.remove(bullet)

    for bulletalian in alien_bullet_list:
        bulletalian.draw(screen)
        bulletalian.move()

    pygame.display.update()
    clock.tick(60)
