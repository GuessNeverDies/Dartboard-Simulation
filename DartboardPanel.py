import pygame as p, random as r
# import DartboardMain # CIRCULAR IMPORT

TOTAL_DARTS = 0
RING_COUNT = [0, 0, 0, 0, 0] #bullseye to missed board
PERCENTAGES = [0, 0, 0, 0, 0]
DARTS = [['N/A', 'no darts thrown yet!']]

def drawDartboard(screen):
    p.draw.rect(screen, 'sienna', (0, 0, 400, 400))
    colorList = ['gray64', 'red', 'green', 'darkgoldenrod1']
    for i in range(-4, 0):
        p.draw.circle(screen, colorList[i], (200, 200), 25*-i)
    p.draw.circle(screen, 'red3', (200, 200), 10)

def throwDarts(screen):
    x = r.randint(0, 400)
    y = r.randint(0, 400)
    dart = p.draw.circle(screen, 'black', (x, y), 2)
    global TOTAL_DARTS, DARTS
    TOTAL_DARTS += 1
    DARTS.append(dart)
    RING_COUNT[calculateLocation(x, y)] += 1
    for i in range(len(RING_COUNT)):
        PERCENTAGES[i] = RING_COUNT[i] * 100 / TOTAL_DARTS
    #print(calculateLocation(x, y))

def calculateLocation(x, y):
    if (((x - 200) ** 2) + ((y - 200) ** 2)) <= 10 ** 2:
        return 0
    elif (((x - 200) ** 2) + ((y - 200) ** 2)) <= 25 ** 2:
        return 1
    elif (((x - 200) ** 2) + ((y - 200) ** 2)) <= 50 ** 2:
        return 2
    elif (((x - 200) ** 2) + ((y - 200) ** 2)) <= 75 ** 2:
        return 3
    else:
        return 4