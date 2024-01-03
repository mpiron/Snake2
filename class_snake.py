import pygame
# Création d'un classe qui représente le serpent.
# Ce snake correspondra à un sprite sur notre jeu.
# Sprite = un élément graphique qui peut se déplacer.

class Snake(pygame.sprite.Sprite):
    # méthode init appelée au chargement de la classe Snake
    # (quand on appelle le serpent)
    # Toutes nos classes commenceront par une majuscule, nos variable en minuscule
	
	
    def __init__(self,surface,x=800,y=600):  # 0.3
	
        #on récupère la superclasse et on appel son constructeur
		
        super().__init__()  # 0.3
        self.width = 30  # 0.3
        self.x = x  # 0.3
        self.y = y  # 0.3
        self.velocity = self.width  # 0.3
        pygame.draw.ellipse(surface, (20, 190, 20), [
            self.x, self.y, self.width, self.width])  # 0.3
			
        # Enregistrer toutes les touches qui sont actionnées par le joueur 
        # pour les récupérer en temps réel dans le boucle et bouger notre serpent 
        self.pressed = {} 
        # dictionnaire vide qui récupère les touches actionnées.
        # un dictionnaire est une ensemble de clés qui sont associées à des valeurs. 
        # exemples: 
		# 			dico={"go":"aller","eat":"manger","two":2}
        # 			pressed={touche_fleche_droite:True, touche_fleche_gauche:False}
