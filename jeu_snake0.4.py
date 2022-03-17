# SNAKE 0.4 : création de fichiers séparés pour les classes
# + gestion des touches qui restent enfoncées (ca ne sera finalement pas utile).
# https://youtu.be/a0kcj6rRQ2s?t=745
# https://youtu.be/a0kcj6rRQ2s?t=1183
# finalement ce système de déplacement n'est pas bon car dans snake,
# on donne une direction et le serpent avance jusqu'à ce qu'on
# change de direction, nous allons corriger ca dans le 0.5
from snake0 import Snake  # Tous les fichiers en minuscules, les classes avec 1 majuscule
import random  # 0.1
import pygame  # 0
pygame.init()  # 0

# initialisation variables
screen_width = 960  # 0.1
screen_height = 720  # 0.1
velocity = 30
apple_x = random.randint(15, screen_width-15)  # 0.1
apple_y = random.randint(15, screen_height-15)  # 0.1

pygame.display.set_caption("Jeu Snake 4TT (version 0.4)")  # 0
# screen est une variable qui correspond à une surface,
screen = pygame.display.set_mode((screen_width, screen_height))  # 0.1
running = True  # 0

# charger le serpent
snake = Snake(screen, screen_width/2, screen_height/2)
clock = pygame.time.Clock()


# La variable apple contiendra l'image de la pomme avec ses dimentions
apple = pygame.image.load("pomme.png")  # 0.1
apple = pygame.transform.scale(apple, (30, 30))  # 0.1
# blit() = injecter une image à un endroit spécifique
screen.blit(apple, (apple_x, apple_y))  # 0.1
# Flip() =  mettre à jour.
pygame.display.flip()  # 0.1

while running:  # 0

    pygame.draw.ellipse(screen, (20, 190, 20), [
        snake.x, snake.y, snake.width, snake.width])  # 0.3
    pygame.display.flip()  # 0.2

    for event in pygame.event.get():  # 0
        if event.type == pygame.QUIT:  # 0
            running = False  # 0
            pygame.quit()  # 0
        elif event.type == pygame.KEYDOWN:   # 0.2
            snake.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            snake.pressed[event.key] = False
        # a partir de maintenant, je sais quelles touches
        # sont actionnées par le joueur.
    # vérifier si le joueur veut déplacer le serpent.
    if snake.pressed.get(pygame.K_RIGHT):
        snake.x += velocity
    elif snake.pressed.get(pygame.K_LEFT):
        snake.x -= velocity
    elif snake.pressed.get(pygame.K_UP):
        snake.y -= velocity
    elif snake.pressed.get(pygame.K_DOWN):
        snake.y += velocity
    pygame.time.delay(100)