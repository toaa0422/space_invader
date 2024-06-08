import math

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

background = pygame.image.load("./background.jpg")
pygame.display.set_caption("space invaders")

icon = pygame.image.load("./spaceship.png")
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load("./player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
#  enemy
# more enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./alien1.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(20)

# bullet
bulletImg = pygame.image.load("./bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
# bullet_change = 0.3
# bullet_change = 20
bullet_state = "ready"

# score
score_val = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10




def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(enemyX, enemyY, i):
    screen.blit(enemyImg[i], (enemyX, enemyY))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 16))


def isCollision(enemyX, enemyY, bulletX, bullletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bullletY, 2)))
    if distance < 27:
        return True
    else:
        return False

font = pygame.font.Font('Faithfull Signature.otf', 80)
over_font = pygame.font.Font('Faithfull Signature.otf', 80)

def show_score(x, y):
    socre = font.render("Score:" + str(score_val), True, (255, 255, 255))
    screen.blit(socre, (x, y))


def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))




while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
                # print("left is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
                # print("right is pressed")
            if event.key == pygame.K_UP:
                playerY_change = -2
                # print("left is pressed")
            if event.key == pygame.K_DOWN:
                playerY_change = 2
            if event.key == pygame.K_SPACE:
                # print("hello")
                bulletX = playerX
                # print(bulletX, bulletY)
                fire_bullet(playerX, bulletY)
                # print("right is pressed")
            # if event.key==pygame.K_q:
            #     print("fk u")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # background
    screen.blit(background, (0, 0))
    # screen.blit(bulletImg, (400, 400))

    # screen.fill((255,255,255))

    # Checking for noundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64:
        playerX = 800 - 64
    elif playerY >= 600 - 64:
        playerY = 600 - 64
    elif playerY <= 0:
        playerY = 0

    # Enemy Movement
    # print(enemyY)
    for i in range(num_of_enemies):

        # game over
        if enemyY[i]>200:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        # playerY[i] += playerY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 800 - 64:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
        # collision

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_val += 1
            print(score_val)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(0, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    # enemy(enemyX, enemyY)
    # enemy(enemyX,enemyY)
    show_score(textX,textY)
    pygame.display.update()
