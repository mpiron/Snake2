# SNAKE 0.3 : et si nous créions une classe snake
# https://youtu.be/a0kcj6rRQ2s?t=88 

import random  # 0.1
import pygame  # 0
pygame.init()  # 0

#création d'un classe qui représente le serpent.
# Ce snake correspondra à un sprite sur notre jeu (vous connaissez les sprites de Scratch) 
# C'est un élément graphique qui peut se déplacer. 
class Snake(pygame.sprite.Sprite):
    # méthode init appelée au chargement de la classe Snake
    # (quand on appelle le serpent)
    # Toutes nos classes commenceront par une majuscule, nos variable en minuscule
    def __init__(self):  # 0.3
        #on récupère la superclasse et on appel son constructeur
        super().__init__()  # 0.3
        self.width = 30  # 0.3
        self.x = screen_width/2  # 0.3
        self.y = screen_height/2  # 0.3
        self.velocity = self.width  # 0.3
        pygame.draw.ellipse(screen, (20, 190, 20), [
            self.x, self.y, self.width, self.width])  # 0.3
    
# initialisation variables
screen_width = 960  # 0.1
screen_height = 720  # 0.1

apple_x = random.randint(15, screen_width-15)  # 0.1
apple_y = random.randint(15, screen_height-15)  # 0.1

pygame.display.set_caption("Jeu Snake 4TT (version 0.3)")  # 0
# screen est une variable qui correspond à une surface,
screen = pygame.display.set_mode((screen_width, screen_height))  # 0.1
running = True  # 0

#charger le serpent
snake = Snake()

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
        if event.type == pygame.KEYDOWN:   # 0.2
            if event.key == pygame.K_UP:  # 0.2
                snake.y -= snake.velocity  # 0.3
            if event.key == pygame.K_DOWN:  # 0.2
                snake.y += snake.velocity  # 0.3
            if event.key == pygame.K_LEFT:  # 0.2
                snake.x -= snake.velocity  # 0.3
            if event.key == pygame.K_RIGHT:  # 0.2
                snake.x += snake.velocity  # 0.3