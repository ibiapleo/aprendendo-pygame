import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.has_collided = False 

    def update(self, *args, **kwargs):
        speed = kwargs.get("obstacle_speed", 5) 
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

def generate_obstacle():
    width = random.randint(30, 70)
    height = random.randint(30, 70)
    x = random.randint(800, 1000)
    y = random.randint(100, 400)
    color = (0, 255, 0)
    return Obstacle(x, y, width, height, color)
