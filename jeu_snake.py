# comprendre et retenir l'idée de
# MODULE / COMPOSANT / METHODE()

# Importation du module pygame
import pygame
# Chargement de tous les composants se trouvant à l'intérieur du module pygame
# Pour ce faire nous utilisons la méthode init()
pygame.init()

# Génération de la fenêtre du jeu
# Utilisation du composant display et de sa méthode set_caption.
pygame.display.set_caption("Jeu Snake 4TT (version 0)")
# Il est possible en 2e argument de mettre une icône pour la fenêtre
# https://youtu.be/8J8wWxbAdFg?t=330

# Création de la fenêtre
# Screen est une surface (nom à connaitre en python)
screen = pygame.display.set_mode((960, 720))

# Boucle permettant de conserver la fenêtre ouverte durant le jeu
running = True
# Création de la boucle du jeu:
print("on commence le jeu")
while running:
    # condition de sortie  = si le joueur ferme la fenêtre avec le "bouton croix"
    # Pour ce faire, nous allons aller chercher dans le module pygame
    # le composant event et la méthode get()
    # Nous allons devoir créer une boucle  FOREACH = pour tous les événements
    for event in pygame.event.get():
        # Fermeture de fenêtre? (nous regardons le type d'événement)
        if event.type == pygame.QUIT:
            # mettre la variable running sur False et quitter le jeu
            running = False
            pygame.quit()
            # petit message dans la console pour voir que nous sommes passé dans if
            print("fermeture du jeu")