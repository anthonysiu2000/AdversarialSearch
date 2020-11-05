import pygame
import sys
import math
import os
import random 
import numpy as np
#create an object for each tile in the gameboard
class Tile:
    #load in images
    images = [
<<<<<<< HEAD
        pygame.image.load(os.path.join(/"imgs", "SmallWumpus.png")),
        pygame.image.load(os.path.join(/"imgs", "SmallWizard.png")),
        pygame.image.load(os.path.join(/"imgs", "SmallHero.png"))
=======
        pygame.image.load(os.path.join("imgs", "SmallWumpus.png")),
        pygame.image.load(os.path.join("imgs", "SmallWizard.png")),
        pygame.image.load(os.path.join("imgs", "SmallHero.png")),
        pygame.image.load(os.path.join("imgs", "SmallWumpusADV.png")),
        pygame.image.load(os.path.join("imgs", "SmallWizardADV.png")),
        pygame.image.load(os.path.join("imgs", "SmallHeroADV.png"))
>>>>>>> 69d1f7b01ecc0f3f0a658dd315013c41e99d9d48
    ]
    def __init__(self, rowval, colval):
        self.unit = "empty"
        self.player = "neutral"
        self.neighbors = []
        self.rowval = rowval
        self.colval = colval
        self.img = self.images[0]

    def show(self, screen, color, w, h, playerType):
        #pygame.draw.rect(screen, color, (self.colval * w, self.colval * w, w, h), 0)
        if playerType == "wumpus":
            self.img = self.images[0]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval*h])
        if playerType == "mage":
            self.img = self.images[1]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval*h])
        if playerType == "hero":
            self.img = self.images[2]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
            #screen.blit(self.img, [self.colval * w, self.rowval * h])
        if playerType == "wumpus-agent":
            self.img = self.images[3]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "mage-agent":
            self.img = self.images[4]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "hero-agent":
            self.img = self.images[5]
            imageRect = self.img.get_rect()
            screen.blit(self.img, (self.colval * w, self.rowval * h), imageRect)
        if playerType == "empty":
            pygame.draw.rect(screen, color, (self.colval * w, self.rowval * h, w, h), 0)
        if playerType == "pit":
            pygame.draw.rect(screen, color, (self.colval * w, self.rowval * h, w, h), 0)
        
        pygame.draw.line(screen, (0,0,0), [self.colval * w, self.rowval*h], [self.colval * w + w, self.rowval*h], 1)
        pygame.draw.line(screen, (0,0,0), [self.colval * w, self.rowval*h], [self.colval * w, self.rowval*h + h], 1)
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
                unit = "mage"

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
                self.board[i][j].neighbors = []

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
    #print("***************")
    #print(str(board[i][j].player) + "-" + str(board[i][j].unit))
    #print("***************")
    if board[j][i].unit == "empty":
        board[i][j].show(screen, (127,127,127), w, h, "empty")
    if board[j][i].unit == "wumpus":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, green, w, h, "wumpus")
        else:
            board[i][j].show(screen, red, w, h, "wumpus-agent")
    if board[j][i].unit == "hero":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, blue, w, h, "hero")
        else:
            board[i][j].show(screen, orange, w, h, "hero-agent")
    if board[j][i].unit == "mage":
        if board[j][i].player == "adversary":
            board[i][j].show(screen, purple, w, h, "mage")
        else:
            board[i][j].show(screen, yellow, w, h, "mage-agent")
    if board[j][i].unit == "pit":
        board[i][j].show(screen, purple, w, h, "pit")

#loops through entire board to create tiles
for i in range(cols):
    for j in range(row):
        showBoardUnit(screen, BOARD.board, i, j)

def matchup(p_type,adv_type):
    if adv_type == "empty" or p_type == "empty":
        return "Win"
    if p_type == adv_type:
        return "draw"
    else:
        if adv_type == "mage":
            if p_type == "wumpus":
                return "Win"
            else:
                return "Loss"
        elif adv_type == "wumpus":
            if p_type == "hero":
                return "Win"
            else:
                return "Loss"
        else:
            if p_type == "mage":
                return "Win"
            else:
                return "Loss"

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
        if destination.player == "adversary":
            selectSecond = False
            print("invalid destination")
            return
        if destination.unit == "pit":
            validDestination = False
            selectSecond = False
            Drow = destination.rowval
            Dcol = destination.colval
            Urow = unitSelected.rowval
            Ucol = unitSelected.colval
            print("you hit a pit")
            BOARD.board[unitSelected.rowval][unitSelected.colval].player = "neutral"
            BOARD.board[unitSelected.rowval][unitSelected.colval].unit = "empty"
            BOARD.setNeighbors()
            #showBoardUnit(screen, BOARD.board, destination., Drow)
            showBoardUnit(screen, BOARD.board, Ucol, Urow)
            pygame.display.update()
            return

        #once verifying destination, unit goes to destination 
        validDestination = False
        selectSecond = False
        Drow = destination.rowval
        Dcol = destination.colval
        Urow = unitSelected.rowval
        Ucol = unitSelected.colval
        print(str(unitSelected.player) + "-" + str(unitSelected.unit))
        print(str(destination.player) + "-" + str(destination.unit))

        #checks unit matchup if unit is able to take an agent's unit
        matchup = "winning"
        if destination.player == "agent":
            if destination.unit == unitSelected.unit:
                matchup = "even"
            if destination.unit == "hero" and unitSelected.unit == "wumpus": 
                matchup = "losing"
            if destination.unit == "wumpus" and unitSelected.unit == "mage": 
                matchup = "losing"
            if destination.unit == "mage" and unitSelected.unit == "hero": 
                matchup = "losing"

        #changes board according to action
        if matchup == "even":
            BOARD.board[Drow][Dcol].player = "neutral"
            BOARD.board[Drow][Dcol].unit = "empty"
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"
        elif matchup == "losing":
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"
        else:
            BOARD.board[Drow][Dcol].player = "adversary"
            BOARD.board[Drow][Dcol].unit = unitSelected.unit
            BOARD.board[Urow][Ucol].player= "neutral"
            BOARD.board[Urow][Ucol].unit = "empty"

        BOARD.setNeighbors()
        print("-----------")
        print(str(unitSelected.player) + "-" + str(unitSelected.unit))
        print(str(destination.player) + "-" + str(destination.unit))
        #updates visualization
        showBoardUnit(screen, BOARD.board, Dcol, Drow)
        showBoardUnit(screen, BOARD.board, Ucol, Urow)
        pygame.display.update()

""""
From this point on we are going to include the ai for the game 
"""
"""
def euclid_dist(p1,p2):
    return  np.sqrt((p1[0]-p2[0])^2 + (p1[1]-p2[1])^2)


def closest_m(pos, peice_type, m_type):
    if m_type = win:
        win_matchups = []  
        for w_m in win_matchups: 
            m_loss = [None]*0
            positions  = move_set(w_m) 
            for moves in position:
                if matchup(moves) == "Loss":
                    m_loss.append(moves) 
        
        if len(m_loss) == 0:
            return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3)) 
        else: 
            
    else:
        draw_matchups = [] 
        return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3))


def static_eval(position,p_type): 
    
    return 0.25 * pieces_left + 0.25 * closest_m(pos,p_type,"draw") 
    + 0.50 * closest_m(pos,p_type,"win")



def move_set(pos): # possible move
    
    p_m= [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0],\
           pos[1]-1], [pos[0]-1, pos[1]+1], [pos[0]+1, 
           pos[1]-1], [pos[0]-1, pos[1]-1],[pos[0]+1, pos[1]+1]]
    
    out_m = [None]*0
    for move in p_m:
        if p_m[0] > 0 and p_m[1] > 0:
            out_m.append(p_m)
            
    return out_m



def minimax(position, tree_depth, maximizingPlayer):
     if tree_depth == 0 or goal(position,p_type): 
         return static_eval(position) #static evaluation
     if maximizingPlayer:
         MaxOut = -inf
         p_moves = mov_set(position)
         for move in p_moves: # all spaces within one move of current pos
             currEval = minimax(move, tree_depth − 1, False)
             MaxOut = max(MaxOut,currEval)
         return MaxOut
     
     else: 
         MinOut = inf
         p_moves = move_set(position)
         for move in p_moves:
             currEval = minimax(move, tree_depth − 1, True)
             MinOut = min(MinOut,currEval)
         return MinOut



def AB_minimax(position, tree_depth, alpha, beta, maximizingPlayer):
     if tree_depth == 0 or goal(position,p_type): 
         return static_eval(position) #static evaluation
     if maximizingPlayer:
         MaxOut = -inf
         p_moves = mov_set(position)
         for move in p_moves: # all spaces within one move of current pos
             currEval = minimax(move, tree_depth − 1, False)
             MaxOut = max(MaxOut,currEval) 
             alpha = max(alpha,currEval) 
             
             if beta < alpha or beta == alpha:
                 break
         
         return MaxOut
     
     else: 
         MinOut = inf
         p_moves = move_set(position)
         for move in p_moves:
             currEval = minimax(move, tree_depth − 1, True)
             MinOut = min(MinOut,currEval)
             beta  = min(beta, currEval)
             if beta < alpha or beta == alpha:
                 break
         return MinOut


"""



#visualization loop
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