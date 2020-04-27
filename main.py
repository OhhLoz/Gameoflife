import random
import time
#import os

DEAD = 0
ALIVE = 1

globalWidth = 0
globalHeight = 0

symbolDictionary = {
    DEAD: ' ',
    ALIVE: u"\u2588" #This symbol is a full square
}

#Initialises an empty grid of size width*height
def zeroInit(width, height):
    global globalHeight, globalWidth
    globalWidth = width
    globalHeight = height
    return [[DEAD for _ in range(height)] for _ in range(width)]

#Initialises a random grid of size width*height using 15% chance of a cell being alive
def randomInit(width, height):
    state = zeroInit(width, height)
    for x in range(0, width):
        for y in range(0, height):
            random_number = random.random()
            if random_number > 0.85:
                state[x][y] = ALIVE
            else:
                state[x][y] = DEAD
    return state

#Actually loops through the current state and draws the appropriate cell state to the screen, using the symbol dictionary at the start of the file. 
def draw(state):
    lines = []
    for y in range(0, globalHeight):
        line = ''
        for x in range(0, globalWidth):
            line += symbolDictionary[state[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)

#This is the main rule method, checking whether a cell should live or die according to the rules of the game
def nextCellValue(cellCoords, state):
    xVal = cellCoords[0]
    yVal = cellCoords[1]
    liveNeighbours = 0

    for currX in range((xVal-1), (xVal+1)+1):
        if currX < 0 or currX >= globalWidth: continue # X Bounds checking

        for currY in range((yVal-1), (yVal+1)+1):
            if currY < 0 or currY >= globalHeight: continue # Y Bounds checking
            if currX == xVal and currY == yVal: continue # Don't count yourself as a neighbour

            if state[currX][currY] == ALIVE:
                liveNeighbours += 1

    if state[xVal][yVal] == ALIVE:
        if liveNeighbours <= 1:# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            return DEAD
        elif liveNeighbours <= 3:# Any live cell with two or three live neighbours lives on to the next generation.
            return ALIVE
        else:
            return DEAD# Any live cell with more than three live neighbours dies, as if by overpopulation.
    else:
        if liveNeighbours == 3:# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            return ALIVE
        else:
            return DEAD

#Using the nextCellValue() method on every cell passed as a parameter into this method, you get the next grid state to be drawn to the screen
def nextGridState(initState):
    nextState = zeroInit(globalWidth, globalHeight)

    for x in range(0, globalWidth):
        for y in range(0, globalHeight):
            nextState[x][y] = nextCellValue((x, y), initState)

    return nextState

#This forever loops the program
def mainLoop(initState):
    nextState = initState
    while True:
        #os.system('clear')
        draw(nextState)
        nextState = nextGridState(nextState)
        time.sleep(0.06)

#This is the actual main method that the system executes, it calls a random state of 100x50 and loops using the method mainLoop()
if __name__ == "__main__":
    initState = randomInit(100, 50)
    draw(initState)
    mainLoop(initState)


# Rules
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.