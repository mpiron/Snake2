import pygame
pygame.init()
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