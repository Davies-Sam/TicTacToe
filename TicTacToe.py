import pygame
from pygame.locals import *
from pygame.constants import (
    QUIT, VIDEORESIZE, HWSURFACE, DOUBLEBUF, RESIZABLE, MOUSEBUTTONDOWN
)

#initialize the game
pygame.init()

# Create the game window
window = pygame.display.set_mode((500,500), HWSURFACE| DOUBLEBUF | RESIZABLE)

# Title, Icon and Text -- Disabled for turn in - don't want to upload a zip with the png. uploading just this .py file instead.
"""
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)
# --- Icons made by "https://www.flaticon.com/authors/ultimatearm" ---

"""
font = pygame.font.Font('freesansbold.ttf', 16)

# Boolean for game loop
gameOver = False

#global variables for the start of game
turns = 0
player = 'X'

# Representation of game board
board = [
    [-9, -8, -7],
    [-6, -5, -4],
    [-3, -2, -1]
]

# restart the game
def resetBoard():
    board[0] = [-9, -8, -7]
    board[1] = [-6, -5, -4]
    board[2] = [-3, -2, -1]

# Check if either player won, Draw a line showing the win
def checkWin():
    if board[0][0] == board[1][1] == board[2][2]:
        pygame.draw.line(window, (255, 0, 0), (0,0), (w,h), 20)
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        pygame.draw.line(window, (255, 0, 0), (0,h), (w,0), 20)
        return True
    elif board[0][0] == board[0][1] == board[0][2]:
        pygame.draw.line(window, (255, 0, 0), (0,h/6), (w,h/6), 20)
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        pygame.draw.line(window, (255, 0, 0), (0,h/2), (w,h/2), 20)
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        pygame.draw.line(window, (255, 0, 0), (0,h - h/6), (w, h - h/6), 20)
        return True
    elif board[0][0] == board[1][0] == board[2][0]:
        pygame.draw.line(window, (255, 0, 0), (w/6,0), (w/6,h), 20)
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        pygame.draw.line(window, (255, 0, 0), (w/2,0), (w/2,h), 20)
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        pygame.draw.line(window, (255, 0, 0), (w - w/6 ,0), (w - w/6,h), 20)
        return True
    else:
        return False

# check for a draw
def checkDraw():
    if not checkWin() and turns == 9:
        return True
    else:
        return False


# Draw Text
def drawText():
    text = font.render("%s's turn" % player, True, (0,255,0), (0,0,255))
    textRect= text.get_rect()
    textRect.center = (w/2,0 + h/20)
    window.blit(text,textRect)
    pygame.display.update()

# Draw board lines
def drawLines():   
    pygame.draw.line(window, (255,255,255), (w/3, 0), (w/3,h))
    pygame.draw.line(window, (255,255,255), (2*w/3, 0), (2*w/3,h))
    pygame.draw.line(window, (255,255,255), (0, h/3), (w,h/3))
    pygame.draw.line(window, (255,255,255), (0, 2*h/3), (w,2*h/3))
    pygame.display.update()


# Check if user wants to play again
def playAgain(num):
    if num == 1:
        text = font.render("%s WON ! SPACE=PLAY AGAIN - OTHER=EXIT" % player, True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (w/2,h/2)
        window.blit(text,textRect)
        pygame.display.update()
    elif num == 0:
        text = font.render("DRAW! SPACE=PLAY AGAIN - OTHER=EXIT", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (w/2,h/2)
        window.blit(text,textRect)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    resetBoard()
                    window.fill((0,0,0))
                    pygame.display.update()
                    return False
                else:
                    return True

# Draw player moves
def drawMoves():
    s = 0
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square != 0:
                if square == 2:
                    pygame.draw.circle(window, (255,255,255), getSquareLocation(s), int(radius/6), 2)
                elif square == 1:
                    topLeft = ( int( getSquareLocation(s)[0] - w/6) , int(getSquareLocation(s)[1] - h/6))
                    topRight = ( int( getSquareLocation(s)[0] + w/6) , int(getSquareLocation(s)[1] - h/6))
                    botLeft = ( int( getSquareLocation(s)[0] - w/6) , int(getSquareLocation(s)[1] + h/6))
                    botRight = ( int( getSquareLocation(s)[0] + w/6) , int(getSquareLocation(s)[1] + h/6))
                    pygame.draw.line(window, (255,255,255), topLeft, botRight)
                    pygame.draw.line(window, (255,255,255), botLeft, topRight)
            s+=1
    pygame.display.update()


def nextPlayer():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

# Update the board
def updateBoard(num, player):
    global turns
    if player == 'X':
        marker = 1
    else:
        marker = 2
    if num == 0:
        if board[0][0] != 1 and board[0][0] != 2:
            board[0][0] = marker
            turns += 1
            nextPlayer()
    elif num == 1:
        if board[0][1] != 1 and board[0][1] != 2:
            board[0][1] = marker
            turns += 1
            nextPlayer()
    elif num == 2:
        if board[0][2] != 1 and board[0][2] != 2:
            board[0][2] = marker
            turns += 1
            nextPlayer()
    elif num == 3:      
        if board[1][0] != 1 and board[1][0] != 2:
            board[1][0] = marker
            turns += 1
            nextPlayer()
    elif num == 4:
        if board[1][1] != 1 and board[1][1] != 2:
            board[1][1] = marker
            turns += 1
            nextPlayer()
    elif num == 5:
        if board[1][2] != 1 and board[1][2] != 2:
            board[1][2] = marker
            turns += 1
            nextPlayer()
    elif num == 6:
        if board[2][0] != 1 and board[2][0] != 2:
            board[2][0] = marker
            turns += 1
            nextPlayer()
    elif num == 7:
        if board[2][1] != 1 and board[2][1] != 2:
            board[2][1] = marker
            turns += 1
            nextPlayer()
    elif num == 8:
        if board[2][2] != 1 and board[2][2] != 2:
            board[2][2] = marker
            turns += 1
            nextPlayer()

# Get Location of square

def getSquareLocation(num):
    
    if num == 0:
        return ( int(w/6) , int(h/6) )
    elif num == 1:
        return ( int(w/2) , int(h/6) )
    elif num == 2:
        return ( int(w - w/6) , int(h/6) )
    elif num == 3:
        return ( int(w/6) , int(h/2) )
    elif num == 4:
        return ( int(w/2) , int(h/2) )
    elif num == 5:
        return ( int(w - w/6) , int(h/2) )
    elif num == 6:
        return ( int(w/6) , int(h - h/6) )
    elif num == 7:
        return ( int(w/2) , int(h - h/6) )
    elif num == 8:
        return ( int(w - w/6) , int(h - h/6) )
    

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
   


# Game Loop

while not gameOver:
    #get new window dimensions
    w, h = pygame.display.get_surface().get_size()

    if w > h:
        radius = h
    else:
        radius = w

    drawText()
    drawLines()
    drawMoves()

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
        elif event.type == VIDEORESIZE:
            window = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        elif event.type == MOUSEBUTTONDOWN:
            square = getSquarefromMouse(pygame.mouse.get_pos())
            updateBoard(square, player)
            drawMoves()
            gameOver = checkWin() or checkDraw()
            if checkDraw():
                gameOver = playAgain(0)
                turns = 0
            elif checkWin():
                gameOver = playAgain(1)
                turns = 0     
            else:
                pass
    pygame.display.update()

            
    