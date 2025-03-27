import pygame
import random
from player import Player
from obstacles import Obstacle, generate_obstacle
from items import Item, generate_item
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


pygame.init()

#config da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Runner Recife")
font = pygame.font.Font(None, 36)

#sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
items = pygame.sprite.Group()

#player
player = Player(100, SCREEN_HEIGHT // 2)
all_sprites.add(player)

#variáveis do jogo
player_life = 3 
sombrinha_time = 0  
pitu_effect_time = 0  
obstacle_speed = 5

#tempo
clock = pygame.time.Clock()

#função para verificar a sombrinha
def apply_sombrinha_effect():
    global sombrinha_time
    if sombrinha_time > 0:
        sombrinha_time -= 1 / FPS  #contar o tempo do efeito
    return sombrinha_time > 0

#função para aplicar o efeito do pitu
def apply_pitu_effect():
    global obstacle_speed, pitu_effect_time
    if pitu_effect_time > 0:
        pitu_effect_time -= 1 / FPS  #contar o tempo do efeito
        if pitu_effect_time <= 0:
            obstacle_speed = 5  # Resetar a velocidade dos obstáculos
    return pitu_effect_time > 0

running = True
game_over = False 
while running:
    screen.fill((0, 0, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        #gera obstáculos e itens aleatoriamente
        if random.randint(1, 100) <= 2:  
            obstacle = generate_obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)
        
        if random.randint(1, 100) <= 5:  
            item = generate_item()
            all_sprites.add(item)
            items.add(item)
    
    #atualizar todos os sprites
    keys = pygame.key.get_pressed()
    all_sprites.update(keys=keys, obstacle_speed=obstacle_speed) 

    #verifica colisões entre o jogador e os objetos coletáveis (itens)
    collected_items = pygame.sprite.spritecollide(player, items, True)
    for item in collected_items:
        if item.type == "bolo_de_rolo":
            player_life += 1  #aumentar vida
        elif item.type == "sombrinha_de_frevo":
            sombrinha_time = 5  #proteção por 5 segundos
        elif item.type == "pitu":
            pitu_effect_time = 5
            if obstacle_speed > 15: #maximo de velocidade
                obstacle_speed = 15  
            obstacle_speed += 2  #aumenta progressivamente a velocidade dos obstáculos

    #verifica colisões entre o jogador e os obstáculos
    for obstacle in pygame.sprite.spritecollide(player, obstacles, False):
        if not obstacle.has_collided and not apply_sombrinha_effect():
            player_life -= 1
            obstacle.has_collided = True  # Marca o obstáculo para não contar novamente
            obstacle.kill()  # Remover obstáculo após a colisão
            if player_life <= 0:
                game_over = True  

    #desenho
    all_sprites.draw(screen)

    # Exibir informações na tela
    life_text = font.render(f"Vida: {player_life}", True, (255, 255, 255))
    screen.blit(life_text, (20, 20))

    speed_text = font.render(f"Velocidade: {obstacle_speed}", True, (255, 255, 255))
    screen.blit(speed_text, (SCREEN_WIDTH - 200, 20))

    if apply_sombrinha_effect():
        sombrinha_text = font.render("Sombrinha Ativada!", True, (255, 255, 0))
        screen.blit(sombrinha_text, (SCREEN_WIDTH // 2 - 100, 50))

    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

    pygame.display.flip() 
    pygame.time.Clock().tick(60)  #60 FPS

pygame.quit()
