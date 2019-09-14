import random
import time

DEAD = 0
ALIVE = 1

globalWidth = 0
globalHeight = 0

def zeroInit(width, height):
    global globalHeight, globalWidth
    globalWidth = width
    globalHeight = height
    return [[DEAD for _ in range(height)] for _ in range(width)]

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

def draw(state):
    symDict = {
        DEAD: ' ',
        ALIVE: '*'
    }
    lines = []
    for y in range(0, globalHeight):
        line = ''
        for x in range(0, globalWidth):
            line += symDict[state[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)

if __name__ == "__main__":
    initState = randomInit(100, 50)
    draw(initState)

# Rules
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.