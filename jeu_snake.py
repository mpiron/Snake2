# SNAKE 0.5 :
# finalement le système de déplacement n'est pas bon car dans snake,
# on donne une direction et le serpent avance jusqu'à ce qu'on
# change de direction, nous corrigeons ça!
from class_snake import Snake  # Tous les fichiers en minuscules, les classes avec 1 majuscule
import random  # 0.1
import pygame  # 0
pygame.init()  # 0

# initialisation variables
screen_width = 960  # 0.1
screen_height = 720  # 0.1
velocity = 30
apple_x = random.randint(15, screen_width-15)  # 0.1
apple_y = random.randint(15, screen_height-15)  # 0.1

pygame.display.set_caption("Jeu Snake 4TT (version 0.5)")  # 0
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
    screen.fill((0, 0, 0))
    screen.blit(apple, (apple_x, apple_y))
    pygame.draw.ellipse(screen, (20, 190, 20), [
        snake.x, snake.y, snake.width, snake.width])  # 0.3
    pygame.display.flip()  # 0.2

    for event in pygame.event.get():  # 0
        if event.type == pygame.QUIT:  # 0
            running = False  # 0
            pygame.quit()  # 0
        elif event.type == pygame.KEYDOWN:   # 0.2
            snake.pressed = event.key
        # à partir de maintenant, je sais quelle touche
        # vient d'être enfoncée
    # vérifier si le joueur veut déplacer le serpent.
    if snake.pressed == pygame.K_RIGHT:                     # 0.5
        snake.x += velocity                                 # 0.5
    elif snake.pressed == pygame.K_LEFT:                    # 0.5
        snake.x -= velocity                                 # 0.5
    elif snake.pressed == pygame.K_UP:                      # 0.5
        snake.y -= velocity                                 # 0.5
    elif snake.pressed == pygame.K_DOWN:                    # 0.5
        snake.y += velocity                                 # 0.5
    pygame.time.delay(100)                                  # 0.4
