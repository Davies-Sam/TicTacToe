import pygame
from pygame.locals import *
from pygame.constants import (
    QUIT, VIDEORESIZE, HWSURFACE, DOUBLEBUF, RESIZABLE, MOUSEBUTTONDOWN
)

#initialize the game
pygame.init()

# Create the game window
window = pygame.display.set_mode((500,500), HWSURFACE| DOUBLEBUF | RESIZABLE)

# Title, Icon and Text
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)
# --- Icons made by "https://www.flaticon.com/authors/ultimatearm" ---
font = pygame.font.Font('freesansbold.ttf', 16)

# Boolean for game loop
gameOver = False

# Representation of game board
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Draw board lines
def drawLines():
    pygame.draw.line(window, (255,255,255), (w/3, 0), (w/3,h))
    pygame.draw.line(window, (255,255,255), (2*w/3, 0), (2*w/3,h))
    pygame.draw.line(window, (255,255,255), (0, h/3), (w,h/3))
    pygame.draw.line(window, (255,255,255), (0, 2*h/3), (w,2*h/3))


# Get Location of square
def getSquareLocation(num):
    if num == 0:
        return ( 0 , int(h/3) )
    elif num == 1:
        return ( 0 , int(w/3) )
    elif num == 2:
        return ( 0 , int(w/3) )
    elif num == 3:
        return ( 0 , int(w/3) )
    elif num == 4:
        return ( int(w/2) , int(h/2) )
    elif num == 5:
        return ( 0 , int(w/3) )
    elif num == 6:
        return ( 0 , int(w/3) )
    elif num == 7:
        return ( 0 , int(w/3) )
    elif num == 8:
        return ( 0 , int(w/3) )
    

# Determine which square the mouse is in
def getSquarefromMouse(x):
    width, height = int(w/3), int(h/3)
    row0height = range(0, height)
    row1height = range(height, 2*height)
    row2height = range(2*height, h)
    col0width = range(0, width)
    col1width = range(width, 2*width)
    col2width = range(2*width, w)
    
    if x[0] in col0width and x[1] in row0height:
        #print("Square 0!")
        return 0
    elif x[0] in col1width and x[1] in row0height:
        #print("Square 1!")
        return 1
    elif x[0] in col2width and x[1] in row0height:
        #print("Square 2!")
        return 2
    elif x[0] in col0width and x[1] in row1height:
        #print("Square 3!")
        return 3
    elif x[0] in col1width and x[1] in row1height:
        #print("Square 4!")
        return 4
    elif x[0] in col2width and x[1] in row1height:
        #print("Square 5!")
        return 5
    elif x[0] in col0width and x[1] in row2height:
        #print("Square 6!")
        return 6
    elif x[0] in col1width and x[1] in row2height:
        #print("Square 7!")
        return 7
    elif x[0] in col2width and x[1] in row2height:
        #print("Square 8!")
        return 8
   

window.fill((0,0,20)) 
# Game Loop
while not gameOver:
    w, h = pygame.display.get_surface().get_size()
    player = "X"
    text = font.render("%s's turn" % player, True, (0,255,0), (0,0,255))
    textRect= text.get_rect()
    textRect.center = (w/2,0 + h/20)
    window.blit(text,textRect)
    if w > h:
        radius = h
    else:
        radius = w
    #window.blit(icon, (w/2,h/2))
    #pygame.draw.circle(window, (255,255,255), (int(w/2), int(h/2)), int(radius/6) ,2)
    drawLines()

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
        elif event.type == VIDEORESIZE:
            window = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        elif event.type == MOUSEBUTTONDOWN:
            square = getSquarefromMouse(pygame.mouse.get_pos())
            squareLoc = getSquareLocation(square)
            #instead of drawing inside this elif, just update the board arrays
            print(squareLoc)
            pygame.draw.circle(window, (255,255,255), squareLoc, int(radius/6) , 2)
            pygame.display.update()
        
    if bool(pygame.mouse.get_focused()):
        getSquarefromMouse(pygame.mouse.get_pos())
    
    pygame.display.update()
    
