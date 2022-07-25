from operator import truediv
import pygame
import random
import math

#Initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 700))

#background
background = pygame.image.load('background.png')

#Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 640
playerX_change = 0
playerY_change = 0

#enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

#bullet
#ready = cant see bullet on screen
#fire = the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 640   
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x  + 16, y + 10))
 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27 :
        return True
    else:
        return False

#Game Loop
running = True
while running:
    
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0, 0) )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #if keystroke is pressed check
        if event.type == pygame.KEYDOWN:

                #left right movement
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                 playerX_change = 1
                
                #bullet movement
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 playerY_change = 0
    #limiting player movement               
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=760:
        playerX = 760
    #enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
    if enemyX[i] <=0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
    elif enemyX[i] >=760:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
    
    enemy(enemyX[i], enemyY[i], i)    
           
    #collision
    collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    if collision:
        bulletY = 640
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)

    #bullet movement
    if bulletY <=0:
        bulletY = 640
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


player(playerX, playerY)       
pygame.display.update()