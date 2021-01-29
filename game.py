''' @author Garrett Starkey
    @version 1.0

Python program utilizing pygame to simulate a game of space invaders.
'''


import pygame

pygame.init()

# the size of the screen
WIDTH = 800
HEIGHT = 600

# Creating the screen.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
background = pygame.image.load('newBackground.png')

# Title, Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('fighter.png')
pygame.display.set_icon(icon)

# Player and Enemy
enemyImg = pygame.image.load('alien.png')
playerImg = pygame.image.load('fighter.png')
enemyX = 380
enemyY = 55
enemyX_change = 0
playerX = 370
playerY = 480
playerX_change = 0

# Add bullets to shoot
bullets = []


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:

    enemyX_change = 9
    # RGB = Red, Blue, Green
    # screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # print("a keystroke has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 766:
        playerX = 766

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX = 0
    elif enemyX >= 766:
        enemyX = 766

    pygame.display.update()
