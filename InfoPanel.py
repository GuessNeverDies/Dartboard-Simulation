import pygame as p, DartboardPanel, ButtonPanel

speed = 20

def drawInfo(screen):
    panel = p.draw.rect(screen, 'white', (400, 0, 300, 400))
    font = p.font.SysFont('Times New Roman', 12)
    texts = ['Number of Darts = ' + str(DartboardPanel.TOTAL_DARTS),
             'Number of rings = ' + str(len(DartboardPanel.RING_COUNT) - 1),
             'Bullseyes hit = ' + str(DartboardPanel.RING_COUNT[0]),
             'Darts missed = ' + str(DartboardPanel.RING_COUNT[-1]),
             'Darts missed % = ' + str(DartboardPanel.PERCENTAGES[4]) + '%',
             'Points = ' + str(DartboardPanel.RING_COUNT[0] * 5 + DartboardPanel.RING_COUNT[1] * 3 + DartboardPanel.RING_COUNT[2] * 2 + DartboardPanel.RING_COUNT[3]),
             'Percent of darts in bullseye = ' + str(DartboardPanel.PERCENTAGES[0]) + '%',
             'Percent of darts hit = ' + str(DartboardPanel.PERCENTAGES[0] + DartboardPanel.PERCENTAGES[1] + DartboardPanel.PERCENTAGES[2] + DartboardPanel.PERCENTAGES[3]) + '%',
             'Speed = ' + str(speed),
             'Recent dart location = ' + str(DartboardPanel.DARTS[-1][0]) + ', ' + str(DartboardPanel.DARTS[-1][1]),
             'Yellow ring hits = ' + str(DartboardPanel.RING_COUNT[1]),
             'Yellow ring hit percent = ' + str(DartboardPanel.PERCENTAGES[1]) + '%',
             'Green ring hits = ' + str(DartboardPanel.RING_COUNT[2]),
             'Green ring hit percent = ' + str(DartboardPanel.PERCENTAGES[2]) + '%',
             'Red ring hits = ' + str(DartboardPanel.RING_COUNT[3]),
             'Red ring hit percent = ' + str(DartboardPanel.PERCENTAGES[3]) + '%']
    for i in range(len(texts)):
        line = font.render(texts[i], True, 'black')
        screen.blit(line, panel.move(5, 20*i))