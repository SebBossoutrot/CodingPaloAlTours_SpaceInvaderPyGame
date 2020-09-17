import pygame
import random
import math

# initialisation de pygame
pygame.init()

# creation d'un écran de jeu
screen = pygame.display.set_mode((800,600))
# X / Y classique

# changement titre et icone
pygame.display.set_caption("Space invaders")
# icon = pygame.image.load('C:/Users/sboss/OneDrive/Documents/Code/Python/SpaceInvader/ufo.png') # dans le cas on l'on se ne trouve pas dans le repertoire
icon = pygame.image.load('SpaceInvader/ufo.png')
pygame.display.set_icon(icon)


# variable du jeu
score = 0
#Couleurs
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,150,0)
RED = (150,0,0)
# Police de caratère
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

# fonction affichage du score

def showScore():
    text = SCORE_FONT.render(str(score), 1, BLACK)
    screen.blit(text, (30, 30))


# Player (~Class)
playerImg = pygame.image.load('SpaceInvader/player.png')
playerX = 370
playerY = 480
playerXChange = 0

def player(x, y):
    screen.blit(playerImg, (x, y))



# Enemy (~Class)
enemyImg = pygame.image.load('SpaceInvader/enemy.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyXChange = 0.15
enemyYChange = 20

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet (~Class)
bulletImg = pygame.image.load('SpaceInvader/bullet.png')
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 1
bulletState = "ready"  #ready on ne vois pas la balle, fire la balle est tirée

def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# ajout d'une fonction pour vérifier si il y collision entre l'enemy et la balle
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2))
    if distance < 27:
        return True
    else:
        return False



# Game Loop (pour que la fenetre reste active tant que l'on ne la ferme pas)
running = True
while running:
    
    # couleur du fond de la fenetre en mode RGB
    screen.fill((100,0,0))
    for event in pygame.event.get():  # methode de capture d'evennements
        if event.type == pygame.QUIT:
            running = False
    # gestion des controles pour le player
        if event.type == pygame.KEYDOWN:
            #print("une toutche a été pressée")
            if event.key == pygame.K_LEFT:
                #print ("fleche gauche")
                playerXChange = -0.3
            if event.key == pygame.K_RIGHT:
                #print ("fleche droite")
                playerXChange = 0.3
            # lancement de la balle
            if event.key == pygame.K_SPACE and bulletState is "ready":
                bulletX = playerX
                fireBullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print ("touche relachée ")
                playerXChange = 0
    
    # pour que ce soit persistent alors dans la boucle
    playerX += playerXChange 

    # ajout des bornes de l'écran
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Mouvement de l'enemy
    enemyX += enemyXChange 

    # ajout des bornes de l'écran
    if enemyX <=0:
        enemyXChange = 0.15
        enemyY += enemyYChange
    elif enemyX >= 736:
        enemyXChange = -0.15
        enemyY += enemyYChange

    # Ajout du mouvement de la balle
    if bulletY <= 0:
        bulletState = "ready"
        bulletY = 480
    if bulletState is "fire":
        fireBullet(bulletX,bulletY)
        bulletY -= bulletYChange


    #collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletState = "ready"
        bulletY = 480
        score += 1
        enemyX = random.randint(0,800)
        enemyY = random.randint(50,150)

    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    showScore()
    pygame.display.update()