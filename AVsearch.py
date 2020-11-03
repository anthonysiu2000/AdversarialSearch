import pygame
import sys
import math
import os
import random 

#create an object for each tile in the gameboard
class Tile:
    def __init__(self, rowval, colval):
        self.unit = "empty"
        self.player = "neutral"
        self.neighbors = []
        self.rowval = rowval
        self.colval = colval

    def show(self, screen, color, w, h):
        pygame.draw.rect(screen, color, (self.colval * w, self.rowval * h, w, h), 0)
        pygame.display.update()

#create a gameboard containing tiles indexed by row and column
class Gameboard:
    def __init__(self, side):
        self.side = side
        self.size = self.side * self.side

        #creates board 2D array of Tiles
        self.board = [[0 for i in range(self.side)] for j in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                self.board[i][j] = Tile(i,j)

    #Set units back to starting point
    def newBoard(self):
        for i in range(self.side):
            unit = "empty"
            if i % 3 == 0:
                unit = "wumpus"
            elif i % 3 == 1:
                unit = "hero"
            else:
                unit = "archer"

            self.board[i][0].unit = unit
            self.board[i][0].player = "agent"
            self.board[i][self.side-1].unit = unit
            self.board[i][self.side-1].player = "adversary"



        
    #creates pits
    def setPits(self):
        for i in range(1, self.side-1):
            #randomly chooses colomn val
            pitcol = random.randint(0, self.side-1)
            self.board[pitcol][i].unit = "pit"



    #sets neighbors for all Tiles
    def setNeighbors(self):
        for i in range(self.side):
            for j in range(self.side):

                #goes through tiles diagonal and adjacent to the tile, and appends to neighbors list
                for k in range(-1, 2):
                    if (i+k < 0) or (i+k >= self.side):
                        continue
                    for l in range(-1, 2):
                        if (k == 0 and l == 0):
                            continue
                        if (j+l < 0) or (j+l >= self.side):
                            continue
                        self.board[i][j].neighbors.append(self.board[i + k][j + l])



    def position(self, value):
    #computes the index of value in the matrix interpreation of the array
        indx = math.floor(value/self.side)
        j = -indx*self.side + value
        if j >= 0:
            return [indx, j]
        return [-1, -1]

    def inv_position(self, i, j):
    #Converts position back to an array value
        if i >= self.side or i < 0:
            return -1
        if j >= self.side or j < 0:
            return -1
        return j + i * self.side
    
    #refreshes a Tile's neighbors. Should be called twice after every move on tiles that change state
    def refresh(self, row, col):

        #changes the tile.neighbors surrounding and including the called tile 
        for i in range(row - 1, row + 2):
            if (i < 0) or (i >= self.side):
                continue
            for j in range(col - 1, col + 2):
                if (j < 0) or (j >= self.side):
                    continue

                #goes through tile's diagonals and adjacents, and appends to neighbors list
                for k in range(-1, 2):
                    if (i+k < 0) or (i+k >= self.side):
                        continue
                    for l in range(-1, 2):
                        if (k == 0 and l == 0):
                            continue
                        if (j+l < 0) or (j+l >= self.side):
                            continue
                        self.board[i][j].neighbors.append(self.board[i + k][j + l])




screen = pygame.display.set_mode((729, 729))

BOARD = Gameboard(9)
BOARD.newBoard()
BOARD.setPits()
BOARD.setNeighbors()


cols = BOARD.side
row = BOARD.side
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
orange = (255, 102, 0)
yellow = (255, 255, 0)
purple = (102, 0, 255)
w = 729 / cols
h = 729 / row

#function used to modify a tile based on unit
def showBoardUnit(screen, board, i, j):
    global w
    global h
    if board[j][i].unit == "empty":
        board[i][j].show(screen, (255,255,255), w, h)
    if board[j][i].unit == "wumpus":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, green, w, h)
        else:
            board[i][j].show(screen, red, w, h)
    if board[j][i].unit == "hero":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, blue, w, h)
        else:
            board[i][j].show(screen, orange, w, h)
    if board[j][i].unit == "archer":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, purple, w, h)
        else:
            board[i][j].show(screen, yellow, w, h)
    if board[j][i].unit == "pit":
        board[i][j].show(screen, (127, 127, 127), w, h)

#loops through entire board to create tiles
for i in range(cols):
    for j in range(row):
        showBoardUnit(screen, BOARD.board, i, j)



selectSecond = False
playerTurn = True
validDestination = False

#variable used to store selected unit
unitSelected = BOARD.board[0][0]

#variable used to store desired location
destination = BOARD.board[0][0]

#when mouse clicks, selects player piece, or its desired location
def mousePress(x):
    global selectSecond
    global playerTurn
    global validDestination
    global unitSelected
    global destination
    global BOARD
    global screen
    a = x[0]
    b = x[1]
    g1 = a // (729 // cols)
    g2 = b // (729 // row)
    #selects player piece on first click
    if selectSecond == False:
        unitSelected = BOARD.board[g1][g2]
        #tests if player clicks on one of their own units, or not
        if unitSelected.player != "adversary":
            print("invalid unit")
            return
        else:
            print("selected unit")
            selectSecond = True

    #selects destination on second click
    else:
        destination = BOARD.board[g1][g2]
        #tests if destination is valid; returns to unit selection if invalid
        for neighbor in unitSelected.neighbors:
            if destination == neighbor:
                print("appropriate destination found")
                validDestination = True
        if validDestination == False:
            selectSecond = False
            print("invalid destination")
            return
        if destination.unit == "pit":
            selectSecond = False
            print("invalid destination")
            return
        if destination.player == "adversary":
            selectSecond = False
            print("invalid destination")
            return
        
        #once verifying destination, unit goes to destination 
        validDestination = False
        selectSecond = False
        Drow = destination.rowval
        Dcol = destination.colval
        Urow = unitSelected.rowval
        Ucol = unitSelected.colval

        BOARD.board[Drow][Dcol].player = "adversary"
        BOARD.board[Drow][Dcol].unit = unitSelected.unit
        BOARD.board[Urow][Ucol].player= "neutral"
        BOARD.board[Urow][Ucol].unit = "empty"
        #BOARD.board.refresh(Drow,Dcol)
        #BOARD.board.refresh(Urow,Ucol)

        showBoardUnit(screen, BOARD.board, Dcol, Drow)
        showBoardUnit(screen, BOARD.board, Ucol, Urow)
        pygame.display.update()


        





loop = True
while loop:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break