import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  #hitbox
        self.image.fill((0, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 5

    def update(self, *args, **kwargs):
        keys = kwargs.get("keys") 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
