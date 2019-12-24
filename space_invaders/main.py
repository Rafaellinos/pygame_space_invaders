"""
pygame     1.9.6
"""
import pygame
import random
import math
from time import sleep
#from pygame import mixer

# intializa the pygame
pygame.init()
pygame.mixer.init()



# Screen game
screen = pygame.display.set_mode((800, 600))  # hori, verti

# Background
background = pygame.image.load("background.png")

# Background sound
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1) # play song in loop


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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    # Enemy default position
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
"""
enemyImg = pygame.image.load('enemy.png')
# Enemy default position
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40
"""
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

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
texX = 10
texY = 10

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score : "+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def player(x, y):
    # drag player into screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):

    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    # distance between enemy and bullet. If is close 27, is collision
    if distance < 27:
        return True
    return

running = True

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
                # Only fire bullet if the state is ready
                if bullet_state is "ready":
                    bullet_sound = pygame.mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Get the current x codinate of the spaceship
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


    # Enemy moviment

    for i in range(num_of_enemies):
        # Game over
        # When enemy reachs the 440 pixels on screen
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 # move enemies away
            game_over_text() # show game over
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = pygame.mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # Respawn enemy
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    player(playerX, playerY)
    show_score(texX, texY)
    pygame.display.update()