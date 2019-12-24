"""
pygame     1.9.6
"""
import pygame
import random

# intializa the pygame
pygame.init()

# Screen game
screen = pygame.display.set_mode((800, 600))  # hori, verti

# Background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space_ship.png')
# Player default position
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
# Enemy default position
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40
running = True

# Bullet

# Ready = u can't see the bulllet on screen
# fire = the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
# Bullet default position
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

running = True


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def player(x, y):
    # drag player into screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
while running:
    # the screen color must be first because otherwise the player will be behind the color.
    # RGB color
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # playerX -= 0.1
    # For each event o pygame event get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if its right or left
        if event.type == pygame.KEYDOWN:
            print("A key has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                print("LEFT pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                print("RIGHT pressed")
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key has been released")
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
