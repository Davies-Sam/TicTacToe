import pygame
from pygame.locals import *
from pygame.constants import (
    QUIT, VIDEORESIZE, HWSURFACE, DOUBLEBUF, RESIZABLE, MOUSEBUTTONDOWN
)

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

def getSquarefromMouse(x):
    width, height = int(w/3), int(h/3)
    row0height = range(0, height)
    row1height = range(height, 2*height)
    row2height = range(2*height, h)
    col0width = range(0, width)
    col1width = range(width, 2*width)
    col2width = range(2*width, w)
    if x[0] in col0width and x[1] in row0height:
        print("Square 0!")
    elif x[0] in col1width and x[1] in row0height:
        print("Square 1!")
    elif x[0] in col2width and x[1] in row0height:
        print("Square 2!")
    elif x[0] in col0width and x[1] in row1height:
        print("Square 3!")
    elif x[0] in col1width and x[1] in row1height:
        print("Square 4!")
    elif x[0] in col2width and x[1] in row1height:
        print("Square 5!")
    elif x[0] in col0width and x[1] in row2height:
        print("Square 6!")
    elif x[0] in col1width and x[1] in row2height:
        print("Square 7!")
    elif x[0] in col2width and x[1] in row2height:
        print("Square 8!")
   
    

# Game Loop
while not gameOver:
    window.fill((0,0,20))
    w, h = pygame.display.get_surface().get_size()
    if w > h:
        radius = h
    else:
        radius = w
    #window.blit(icon, (w/2,h/2))
    #pygame.draw.circle(window, (255,255,255), (int(w/2), int(h/2)), int(radius/6) ,2)
    pygame.draw.line(window, (255,255,255), (w/3, 0), (w/3,h))
    pygame.draw.line(window, (255,255,255), (2*w/3, 0), (2*w/3,h))
    pygame.draw.line(window, (255,255,255), (0, h/3), (w,h/3))
    pygame.draw.line(window, (255,255,255), (0, 2*h/3), (w,2*h/3))

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
        elif event.type == VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
            screen.blit(pygame.transform.scale(icon,event.dict['size']),(0,0))
            #pygame.display.flip()

    getSquarefromMouse(pygame.mouse.get_pos())
    
    pygame.display.flip()
    
