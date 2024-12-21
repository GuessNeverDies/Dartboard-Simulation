import pygame as p

LABELS = ['  START', '   STOP', '  RESET', ' FASTER', 'SLOWER']
COLORS = ['green', 'red', 'yellow', 'blue', 'maroon']
NUM_OF_BUTTONS = len(LABELS)
BUTTON_WIDTH = 400 // NUM_OF_BUTTONS

def drawButtons(screen):
    panel = p.draw.rect(screen, 'gray', (0, 400, 400, 500))
    font = p.font.SysFont('Times New Roman', 20)
    buttons = []
    template = p.Rect(0, 0, BUTTON_WIDTH, 50)
    for i in range(NUM_OF_BUTTONS):
        button = template.clamp(panel).move(i*BUTTON_WIDTH, 25)
        p.draw.rect(screen, COLORS[i], button)
        line = font.render(LABELS[i], True, 'black')
        screen.blit(line, button.move(0, 12))
        screen.blit(line, button.move(1, 12))
        buttons.append(button)
    return buttons