# SNAKE 0.2 : déplacer le serpent (l'ellipse)

import random  # 0.1
import pygame  # 0
pygame.init()  # 0

# initialisation variables
screen_width = 960  # 0.1
screen_height = 720  # 0.1

snake_width = 30  # 0.1
snake_x = screen_width/2  # 0.1
snake_y = screen_height/2  # 0.1
snake_velocity = snake_width  # 0.2

apple_x = random.randint(15, screen_width-15)  # 0.1
apple_y = random.randint(15, screen_height-15)  # 0.1

pygame.display.set_caption("Jeu Snake 4TT (version 0.2)")  # 0
# screen est une variable qui correspond à une surface,
screen = pygame.display.set_mode((screen_width, screen_height))  # 0.1
running = True  # 0

# affichage du serpent (ellipse plutôt que carré)
pygame.draw.ellipse(screen, (20, 190, 20), [
    snake_x, snake_y, snake_width, snake_width])  # 0.1

# La variable apple contiendra l'image de la pomme avec ses dimentions
apple = pygame.image.load("pomme.png")  # 0.1
apple = pygame.transform.scale(apple, (30, 30))  # 0.1
# blit() = injecter une image à un endroit spécifique
screen.blit(apple, (apple_x, apple_y))  # 0.1
# Flip() =  mettre à jour.
pygame.display.flip()  # 0.1


while running:  # 0

    pygame.draw.ellipse(screen, (20, 190, 20), [
        snake_x, snake_y, snake_width, snake_width])  # 0.2
    pygame.display.flip()  # 0.2

    for event in pygame.event.get():  # 0
        if event.type == pygame.QUIT:  # 0
            running = False  # 0
            pygame.quit()  # 0
        if event.type == pygame.KEYDOWN:   # 0.2
            if event.key == pygame.K_UP:  # 0.2
                snake_y -= snake_velocity  # 0.2
            if event.key == pygame.K_DOWN:  # 0.2
                snake_y += snake_velocity  # 0.2
            if event.key == pygame.K_LEFT:  # 0.2
                snake_x -= snake_velocity  # 0.2
            if event.key == pygame.K_RIGHT:  # 0.2
                snake_x += snake_velocity  # 0.2
