import pygame
from pygame.locals import *
#initialize the game
pygame.init()

# Create the game window
window = pygame.display.set_mode((500,500), HWSURFACE| DOUBLEBUF | RESIZABLE)

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)
# --- Icons made by "https://www.flaticon.com/authors/ultimatearm" ---

# Boolean for game loop
gameOver = False

# Representation of game board
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Game Loop
while not gameOver:
    window.fill((0,0,20))
    w, h = pygame.display.get_surface().get_size()
    window.blit(icon, (w/2,h/2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            screen.blit(pygame.transform.scale(icon,event.dict['size']),(0,0))
            #pygame.display.flip()

    
    pygame.display.flip()
    
