# SNAKE 0.1 : affichage d'une pomme et d'un carré = début du serpent
# Nous allons donc apprendre à afficher une image!
# Rappel de l'utilisation du module random
# Utilisation de
#   surface = pygame.display.set_mode((long,larg))
#   pygame.draw.ellipse(où, couleur, [up_x,up_y,largeur,hauteur])
#   pygame.draw.rect(où, couleur, [up_x,up_y,largeur,hauteur])
#   apple = pygame.image.load("pomme.png")
#   apple = pygame.transform.scale(apple, (30, 30))
#   screen.blit(apple, (apple_x, apple_y))   = on colle un sticker qqpart sur la surface
#   REM: apparemment to blit, se traduit en "transferer par bloc"
#   pygame.display.flip()     = mise à jour

import random
import pygame  # 0
pygame.init()  # 0

# initialisation variables
screen_width = 960  # largeur de l'affichage
screen_height = 720  # hauteur de l'affichage

# Variable du serpent centré dans la fenêtre
# L'épaisseur du serpent correspond au nombre de pixels
snake_width = 30
snake_x = screen_width/2
snake_y = screen_height/2
apple_x = random.randint(0, screen_width-30)
apple_y = random.randint(0, screen_height-30)


pygame.display.set_caption("Jeu Snake 4TT (version 0.1)")  # 0
# screen est une variable qui correspond à une surface,
# nous en aurons besoin pour y afficher des éléments (la pomme par exemple).
# en effet, la méthode set_mode renvoit une surface
screen = pygame.display.set_mode((screen_width, screen_height))  # 0,1
running = True  # 0

# affichage du serpent (ellipse plutôt que carré)
pygame.draw.ellipse(screen, (20, 190, 20), [
    snake_x, snake_y, snake_width, snake_width])
pygame.draw.ellipse(screen, (190, 20, 20), [
    snake_x/2, snake_y/2, snake_width*2, snake_width])
pygame.draw.ellipse(screen, (20, 20, 190), [
    screen_width/4*3, screen_height/2, snake_width*3, snake_width])
# création d'une nourriture pour le serpent
# J'utilise la module pygame, le composant image et la méthode load()
# convert_alpha est une méthode que j'applique au composant image.
# La variable apple contiendra la pomme
apple = pygame.image.load("pomme.png")
# Je réduis la taille de mon image
apple = pygame.transform.scale(apple, (30, 30))
# la méthode blit() d'un composant surface permet d'injecter une image à un endroit spécifique
screen.blit(apple, (apple_x, apple_y))
# il faut également mettre à jour notre écran
# Nous utilisons alors la méthode flip agissant sur le composant display du module pygame.
# Flip = retourner ou plutôt mettre à jour.
pygame.display.flip()


while running:  # 0
    for event in pygame.event.get():  # 0
        if event.type == pygame.QUIT:  # 0
            running = False  # 0
            pygame.quit()  # 0
