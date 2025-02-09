import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(Enemy, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surf = pygame.image.load('Svg_example3.svg')
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(0, self.WIDTH), 25))
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.WIDTH:
            self.kill()
