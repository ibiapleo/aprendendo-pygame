import pygame
import random
import os

from config import SCREEN_WIDTH

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, item_type):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = item_type
        
    def update(self, *args, **kwargs):
        speed = kwargs.get("obstacle_speed", 5)
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

            

def generate_item():
    y_positions = [250, 300, 350]
    item_types = {
        "bolo_de_rolo": "../assets/bolo.webp",
        "sombrinha_de_frevo": "../assets/erasebg-transformed.webp",
        "pitu": "../assets/pitu.webp"
    }
    item_type = random.choice(list(item_types.keys()))
    return Item(SCREEN_WIDTH, random.choice(y_positions), item_types[item_type], item_type)
