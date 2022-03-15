import pygame
import random
pygame.init()#commandes de jeu qui vont arriver

plat_largeur = 1500#largeur du plateau
plat_hauteur = 900#hauteur du plateau
#Important, cette variable sera sans doute très important par la suite. 
plateau = pygame.display.set_mode((plat_largeur,plat_hauteur))#création du plateau
pygame.display.set_caption("Snake Le Jeu de Mme Piron")#Nom du jeu
#info_ecran=pygame.display.info()  trouvé par Anton pour une affichage en plein écran
#https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame

ColorSnake = (60, 60, 90)
ColorFond = (232, 255, 0)
ColorEcriture = (0, 0, 0)
ColorPomme = (60, 60, 90)
Jaune = (255, 255, 200)
Rouge = (255, 200, 200)
Vert = (200, 255, 150)
Bleu = (200, 200, 255)
Rose = (255, 200, 255)

liste_couleur = [Jaune, Rouge, Vert, Bleu, Rose]

#X1 et y1 donnent la position du snake au démarrage (au milieu)
#... erreur de ma part, à comprendre plus tard
x1 = plat_largeur/2
y1 = plat_hauteur/2

vitesse = 5
bloc_serpent = 50

pomme = pygame.image.load("pomme.png").convert_alpha()
#ajout _alpha pour obtenir une transparence du PNG
pommetaille = pygame.transform.scale(pomme, (bloc_serpent,bloc_serpent))

x1_change = 0
y1_change = 0
 
#à expliquer, quel est l'intérêt???
clock = pygame.time.Clock()

police_ecriture = pygame.font.SysFont("Arial",60)

def message(msg, color):
    mesg = police_ecriture.render(msg, True, color)
    dimension = mesg.get_rect()
    plateau.blit(mesg,[plat_largeur/2-dimension.width/2, plat_hauteur/2-dimension.height/2])
    
def mon_score(score):
    score_py = police_ecriture.render("Points : " + str(score), True, (150,150,150))
    plateau.blit(score_py, [0,0])
    
def mon_serpent(liste_serpent,color):
    for carre in liste_serpent:
        pygame.draw.rect(plateau, color, [carre[0], carre[1], bloc_serpent, bloc_serpent])
    
    
def gameLoop():
    game_over = False
    game_stop = False
    x1 = plat_largeur/2
    y1 = plat_hauteur/2
    x1_change = 0
    y1_change = 0
    couleurSerpent = 0 #numéro dans la liste des couleurs 
    score = 0
    foodx = round(random.randrange(0, plat_largeur-bloc_serpent)/bloc_serpent)*bloc_serpent
    foody = round(random.randrange(0, plat_hauteur-bloc_serpent)/bloc_serpent)*bloc_serpent

    r = 0
    g = 255
    b = 0

    liste_serpent =[]
    longueur_serpent = 1
    while not game_over:
        multicolore = (r,g,b)
        while game_stop==True:
            plateau.fill(ColorFond)
            message("Dommage -_-      ESPACE = rejouer     ESCAPE = quitter", ColorEcriture)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_stop = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:    
                if event.key==pygame.K_UP:
                    x1_change = 0
                    y1_change =-bloc_serpent
                if event.key==pygame.K_DOWN:
                    x1_change = 0
                    y1_change = bloc_serpent            
                if event.key==pygame.K_LEFT:
                    x1_change =-bloc_serpent
                    y1_change = 0            
                if event.key==pygame.K_RIGHT:
                    x1_change = bloc_serpent
                    y1_change = 0
        if y1<0 or x1>=plat_largeur or x1<0 or y1>=plat_hauteur:
            game_stop = True
        x1 += x1_change
        y1 += y1_change   
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, plat_largeur-bloc_serpent)/bloc_serpent)*bloc_serpent
            foody = round(random.randrange(0, plat_hauteur-bloc_serpent)/bloc_serpent)*bloc_serpent
            score += 1  
            longueur_serpent += 1
            couleurSerpent += 1
        plateau.fill(liste_couleur[couleurSerpent%len(liste_couleur)])
        # pygame.draw.rect(plateau,ColorPomme ,[foodx, foody, bloc_serpent, bloc_serpent])
        pomme_rect = pommetaille.get_rect(topleft=(foodx,foody))
        plateau.blit(pommetaille, (pomme_rect))
        tete_serpent = []
        tete_serpent.append(x1)
        tete_serpent.append(y1)
        liste_serpent.append(tete_serpent)
        if len(liste_serpent) > longueur_serpent:
            del liste_serpent[0]
        for carre in liste_serpent[:-1]:
            if carre == tete_serpent:
                game_stop = True
    
        
        mon_serpent(liste_serpent,multicolore)
        mon_score(score)
        pygame.display.update()
        
        clock.tick(vitesse)    
        

 

    pygame.quit()
    
gameLoop()