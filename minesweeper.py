import pygame
from random import randint
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACKGRAY = (100, 100, 100)
WHITEGRAY = (160, 160, 160)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
TOPY = 100 
ROWS = 31
COLUMNS = 16
NUMBEROFBOMS = 99
SIZEOFSQUARE = 50

class Square:
    def __init__(self, surface, x, y, sizeOfSquare, board, hasBomb = False, number = 0):
        self.surface = surface
        self.isShown = False
        self.hasBomb = hasBomb
        self.number = number
        self.isFlagged = False
        self.x = x
        self.y = y
        self.coordinates = (x * sizeOfSquare, y * sizeOfSquare + TOPY)
        self.sizeOfSquare = sizeOfSquare
        self.neighbours = []
        self.board = board


    def show(self):
        if self.isShown:
            pass
        else:
            self.isShown = True
            self.board.shown += 1
            #print(self.board.shown)
        

    def flag(self):
        if self.isFlagged:
            self.isFlagged = False
            pygame.draw.rect(self.surface, BLACK, (self.coordinates[0] +1 , self.coordinates[1] +1, self.sizeOfSquare -1, self.sizeOfSquare -1))
            self.board.flagsLeft += 1
        else:
            self.isFlagged = True
            self.board.flagsLeft -= 1

    def draw(self):
        global lost
        pygame.font.init()
        font = pygame.font.Font('FFFFORWA.TTF', 32)
        text = str(self.board.board[self.x][self.y])
        if self.mouseOn():
            pass
            # pygame.draw.rect(self.surface, BLACKGRAY, (self.coordinates[0] +1 , self.coordinates[1] +1, self.sizeOfSquare -1, self.sizeOfSquare -1))
            # pygame.display.update()
        if self.isShown:
            if text == '1':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, BLUE)
                self.board.blankClick = False
            elif text == '2':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, GREEN)
                self.board.blankClick = False
            elif text == '3':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, (255, 180, 180))
                self.board.blankClick = False
            elif text == '4':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, (255, 130, 130))
                self.board.blankClick = False
            elif text == '5':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, (140, 0, 0))
                self.board.blankClick = False
            elif text == '6':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, (50, 0, 0))
                self.board.blankClick = False

            elif text == 'X':
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, BLACK)
                self.board.blankClick = False
                lost =  True
            elif text == '0':
                self.board.blankClick = True
                # pygame.draw.rect(self.surface, WHITEGRAY, (self.coordinates[0] +1 , self.coordinates[1] +1, self.sizeOfSquare -1, self.sizeOfSquare -1))
                self.clickingOnBlank()
                # self.draw()
                
            else:
                textsurface = font.render(str(self.board.board[self.x][self.y]), False, WHITE)
                self.board.blankClick = False
            try:  
                squareBackground(self.surface, text, self.coordinates, self.sizeOfSquare, self.isFlagged)
                self.surface.blit(textsurface, (self.coordinates[0] + 15, self.coordinates[1] + 5))
                
                
            except:
                pass
            pass
        
        if self.isFlagged:
            #textsurface = font.render('#', False, (WHITE))
            #self.surface.blit(textsurface, (self.coordinates[0] + 15, self.coordinates[1] + 5))
            drawFlag(self.surface, self.coordinates[0], self.coordinates[1])
            # print(self.board.showing)
            self.board.blankClick = False

            
    def mouseOn(self):
        global mousePos
        global mouseClick
        if self.isShown:
            return False

        x = self.coordinates[0]
        y = self.coordinates[1]
        mouseX = mousePos[0]
        mouseY = mousePos[1]

        if mouseX >= x and mouseX < x + self.sizeOfSquare:
            if mouseY >= y and mouseY < y + self.sizeOfSquare:
                try:
                    if mouseClick == (1, 0, 0) and (not self.isFlagged) and (not self.isShown) and (not lost):
                        self.show()
                    elif mouseClick == (0, 0, 1) and (not self.isShown) and (not lost):
                        self.flag()
                    mouseClick = (0, 0, 0)
                except:
                    pass
                
                return True
        
        return False


    def clickingOnBlank(self):
        self.neighbours = []
        x = self.x
        y = self.y

        try:
            if x != 0 and y != 0: 
                self.board.squares[x - 1][y - 1].show()  
                # self.repeat()        
        except:
            pass
        try:
            if y != 0:
                self.board.squares[x][y - 1].show()
                # self.repeat() 
        except:
            pass
        try:
            if y != 0:
                self.board.squares[x + 1][y - 1].show()
                # self.repeat() 
        except:
            pass
    
        try:
            if x != 0:
                self.board.squares[x - 1][y].show()
                # self.repeat()
            
        except:
            pass
        try:
            self.board.squares[x + 1][y].show()
            # self.repeat() 
        except:
            pass

        try:
            if x != 0:
                self.board.squares[x - 1][y + 1].show()
                # self.repeat() 
        except:
            pass
        try:
            self.board.squares[x][y + 1].show()
            # self.repeat()
            
        except:
            pass
        try:
            self.board.squares[x + 1][y + 1].show()
            # self.repeat() 
        except:
            pass

        '''
        for i in range(0, len(self.board.showing)):
            u = self.board.squares[self.board.showing[i][0]][self.board.showing[i][1]]
            #if u.isShown:
            u.draw()
        '''
        


class Board:
    def __init__(self, surface, rows, columns, sizeOfSquare):
        self.surface = surface
        self.rows = rows
        self.columns = columns
        self.sizeOfSquare = sizeOfSquare
        self.board = []
        self.squares = []
        self.numberOfBombs = NUMBEROFBOMS
        self.blankClick = False
        self.flagsLeft = self.numberOfBombs
        self.shown = 0
    
    def create(self):
        for x in range(0, self.rows):
            self.board.append([])
            for y in range(0, self.columns):
                self.board[x].append(0)
        
        def defineNum():
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    if self.board[i][j] == 'X':
                        try:
                            if i != 0 and j != 0:
                                self.board[i-1][j-1] += 1
                        except:
                            pass

                        try:
                            if i != 0:
                                self.board[i-1][j] += 1
                        except:
                            pass

                        try:
                            if i != 0:
                                self.board[i-1][j+1] += 1
                        except:
                            pass

                        try:
                            if j != 0:
                                self.board[i][j-1] += 1
                        except:
                            pass

                        try:
                            self.board[i][j+1] += 1
                        except:
                            pass

                        try:
                            if j != 0:
                                self.board[i+1][j-1] += 1
                        except:
                            pass

                        try:
                            self.board[i+1][j] += 1
                        except:
                            pass

                        try:
                            self.board[i+1][j+1] += 1
                        except:
                            pass


        def randomBombs():
            counter = 0
            global firstX
            global firstY
            while counter != self.numberOfBombs:
                bombx = randint(0, self.rows - 1)
                bomby = randint(0, self.columns - 1)
                if self.board[bombx][bomby] != 'X' and bombx != firstX and bomby != firstY:
                    if bombx == (firstX-1) and bomby == (firstY - 1):
                        pass
                    elif bombx == (firstX) and bomby == (firstY):
                        pass
                    elif bombx == (firstX+1) and bomby == (firstY + 1):
                        pass
                    elif bombx == (firstX) and bomby == (firstY - 1):
                        pass
                    elif bombx == (firstX) and bomby == (firstY +1):
                        pass
                    elif bombx == (firstX+1) and bomby == (firstY-1):
                        pass
                    elif bombx == (firstX+1) and bomby == (firstY):
                        pass
                    elif bombx == (firstX-1) and bomby == (firstY + 1):
                        pass
                    else:
                        counter += 1
                        self.board[bombx][bomby] = 'X'
                    
                    
            #print(firstX)
            #print(firstY)
        randomBombs()
        defineNum()

        for x in range(0, self.rows):
            self.squares.append([])

        for x in range(0, self.rows):
            for y in range(0, self.columns):
                if self.board[x][y] == 'X':
                    self.squares[x].append(Square(self.surface, x, y, self.sizeOfSquare, self, True))
                else:
                    self.squares[x].append(Square(self.surface, x, y, self.sizeOfSquare, self, number = self.board[x][y]))
        
    def draw(self):     
        global mousePos
        if self.blankClick:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.squares[i][j].isShown:
                        self.squares[i][j].draw()      
        x = int(mousePos[0] / self.sizeOfSquare)
        y = int((mousePos[1] - TOPY) / self.sizeOfSquare)

        try:
            self.squares[x][y].draw()
        except:
            pass
        
    

    
    def showBombs(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if self.board[i][j] == 'X':
                    self.squares[i][j].show()

        self.blankClick = True   
        self.draw()
    


class Timer:
    def __init__(self):
        self.accumulated_time = 0
        self.start_time = pygame.time.get_ticks()
        self.running = True

    def pause(self):
        if not self.running:
            raise Exception('Timer is already paused')
        self.running = False
        self.accumulated_time += pygame.time.get_ticks() - self.start_time

    def resume(self):
        if self.running:
            raise Exception('Timer is already running')
        self.running = True
        self.start_time = pygame.time.get_ticks()

    def get(self):
        if self.running:
            return (self.accumulated_time +
                    (pygame.time.get_ticks() - self.start_time))
        else:
            return self.accumulated_time


class Button:
    pygame.font.init()
    def __init__(self, surface, coordinates, width, height, text, font = pygame.font.SysFont('Comic Sans MS', 29)):
        self.surface =surface
        self.position = coordinates
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.outsideColor = WHITE
        self.insideColorOut = BLACK
        self.insideColorIn = WHITEGRAY


    def isMouseOn(self):
        global mousePos
        try:
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            positionX = self.position[0]
            positionY = self.position[1]

            if mouseX >= positionX and mouseX <= positionX + self.width:
                if mouseY >= positionY and mouseY <= positionY + self.height:
                    return True
        except:
            pass
        return False


    def clicked(self):
        if self.isMouseOn() and mouseClick == (1, 0, 0):
            return True
        return False


    def draw(self):
        # Outside Box
        pygame.draw.rect(self.surface, self.outsideColor, (self.position[0], self.position[1], self.width, self.height))

        # Inside Box
        if self.isMouseOn():
            pygame.draw.rect(self.surface, self.insideColorIn, (self.position[0] + 5, self.position[1] + 5, self.width - 10, self.height - 10))
        else:
            pygame.draw.rect(self.surface, self.insideColorOut, (self.position[0] + 5, self.position[1] + 5, self.width - 10, self.height - 10))

        #Text
        # pygame.font.init()
        #font = pygame.font.Font('FFFFORWA.TTF', 32)
        textsurface = self.font.render(self.text, False, self.outsideColor)
        self.surface.blit(textsurface, (self.position[0] + 17, self.position[1] + 4))
        pygame.display.update()


def squareBackground(surface, text, coordinates, sizeOfSquare, flagged):
    if text != 'X':
        pygame.draw.rect(surface, WHITEGRAY, (coordinates[0] +1 , coordinates[1] +1, sizeOfSquare -1, sizeOfSquare -1))
    elif not flagged:
        pygame.draw.rect(surface, RED, (coordinates[0] +1 , coordinates[1] +1, sizeOfSquare -1, sizeOfSquare -1))
    else:
        pygame.draw.rect(surface, GREEN, (coordinates[0] +1 , coordinates[1] +1, sizeOfSquare -1, sizeOfSquare -1))
    pass



def drawFlag(surface, x, y):
    pygame.draw.rect(surface, WHITE, (x + 36, y+ 25, 4, 15))
    pygame.draw.polygon(surface, RED, ((x+10, y+20), (x+40, y+10), (x+40, y+30)))
    # pygame.draw.rect(surface, WHITE, (x + 45, y+ 25, 2, 15))



def drawGrid(surface, rows, columns, sizeOfSquare):

    for x in range(0, rows + 1):
        for y in range(0, columns + 1):
            pygame.draw.line(surface, WHITE, (x * sizeOfSquare, TOPY), (x * sizeOfSquare, y * sizeOfSquare + TOPY))
            pygame.draw.line(surface, WHITE, (0, y* sizeOfSquare + TOPY), (x * sizeOfSquare, y * sizeOfSquare + TOPY))
    
    # pygame.display.update()

def checkMouse(board, sizeOfSquare):
    global mouseClick
    global mousePos
    global clickCounter

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick = pygame.mouse.get_pressed()
            if clickCounter == 0 and mouseClick == (1, 0, 0) and mousePos[1] > TOPY:
                global firstX
                global firstY
                firstX = mousePos[0] // sizeOfSquare
                firstY = (mousePos[1] - TOPY) // sizeOfSquare
                clickCounter += 1
                board.create()

def win(board):
        n = board.rows * board.columns
        if board.shown == n - board.numberOfBombs:
            print('You won')
            return True
        return False

def printFlagsLeft(surface, board, width, height):
    pygame.font.init()
    font = font = pygame.font.Font('FFFFORWA.TTF', 35)
    if board.flagsLeft > 9 or board.flagsLeft < 0:
        textsurface = font.render(str(board.flagsLeft), False, WHITE)
    else:
        textsurface = font.render(' ' + str(board.flagsLeft), False, WHITE)
    pygame.draw.rect(surface, BLACK, (0, 0, width, TOPY))
    surface.blit(textsurface, (width-100, TOPY-70))
    # pygame.display.update()


def printTime(surface, clock):
    pygame.font.init()
    font = font = pygame.font.Font('FFFFORWA.TTF', 35)
    time = int(clock.get() // 1000)

    minutes = time // 60
    seconds = time % 60
    if seconds < 10:
        text = str(minutes) + ':' + '0' + str(seconds)
    else:
        text = str(minutes) + ':' + str(seconds)

    if len(text) == 1:
        textsurface = font.render('' + text, False, WHITE)
    elif len(text) == 2:
        textsurface = font.render(' ' + text, False, WHITE)
    elif len(text) == 3:
        textsurface = font.render(' ' + text, False, WHITE)
    elif len(text) == 4:
        textsurface = font.render(' ' + text, False, WHITE)
    surface.blit(textsurface, (50, TOPY-70))


def topBar(surface, clock, board, width, height, rows, columns, sizeOfSquare):
    global clickCounter
    global lost
    global restart
    printFlagsLeft(surface, board,width, height)
    printTime(surface, clock)
    restart =  Button(surface, (width//2 - 25, 25), 50, 50, ':)' )
    if restart.isMouseOn():
        restart.text = ':('
    if lost:
        restart.text = ':('
        try:
            clock.pause()
        except:
            pass
    if restart.clicked():
        clock.accumulated_time = 0
        try:
            clock.resume()
        except:
            pass
        clickCounter = 0
        lost = True

    restart.draw()

def main():

    columns = COLUMNS
    rows = ROWS
    sizeOfSquare = SIZEOFSQUARE
    width = rows * sizeOfSquare + 1
    height = columns * sizeOfSquare + 1 + TOPY

    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Minesweeper')
    icon = pygame.image.load('image.png')
    pygame.display.set_icon(icon)

    running = True
    global lost
    # global blankClick
    lost = False
    # global board
    global clickCounter
    clickCounter = 0
    global mouseClick
    clock = Timer()


    board = Board(surface, rows, columns, sizeOfSquare)
    # board.create()
    while running:
        checkMouse(board, sizeOfSquare)
        #surface.fill(BLACK)
        #board.drawShown()
        drawGrid(surface, rows, columns, sizeOfSquare) 
        board.draw()
        topBar(surface, clock, board, width, height, rows, columns, sizeOfSquare)

        pygame.display.update()
        if lost:
            board.showBombs()
            pygame.display.update()
            
            if restart.clicked():
                clickCounter = 0
                surface.fill(BLACK)
                drawGrid(surface, rows, columns, sizeOfSquare)
                # print('ai')
                board = Board(surface, rows, columns, sizeOfSquare)
                topBar(surface, clock, board, width, height, rows, columns, sizeOfSquare)
                checkMouse(board, sizeOfSquare)
                lost = False

                
        if win(board):
            sleep(3)
            clickCounter = 0
            surface.fill(BLACK)
            drawGrid(surface, rows, columns, sizeOfSquare)
            # print('ai')
            board = Board(surface, rows, columns, sizeOfSquare)
            checkMouse(board, sizeOfSquare)

        pygame.time.delay(1)
        mouseClick = (0,0,0)
        # blankClick = False
        


main()