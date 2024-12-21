"""
This program is the minimum code we need to use pygame.
Without adding anything else, this will open a pygame window and
allow it to close properly. The window will be blank.
"""

import pygame as p
import DartboardPanel
import ButtonPanel
import InfoPanel

def setup():
    global screen, clock
    p.init()  # initialize all pygame stuff
    screen = p.display.set_mode((700, 500))  # create display object
    clock = p.time.Clock()  # create time object


def main():
    setup()  # call the setup function that we defined above
    DartboardPanel.drawDartboard(screen)
    buttons = ButtonPanel.drawButtons(screen) #buttons list of rectangles [START, STOP, RESET]
    done = dartsOn = False
    while not done:  # loop continues until done = True
        for event in p.event.get():  # iterate through event queue
            if event.type == p.QUIT:  # if we click the red X to close the window
                done = True  # end loop
            elif event.type == p.MOUSEBUTTONDOWN:
                click = p.mouse.get_pos()
                #print(click)
                if buttons[0].collidepoint(click): # If I click on the green button
                    dartsOn = True
                elif buttons[1].collidepoint(click):
                    dartsOn = False
                elif buttons[2].collidepoint(click):
                    dartsOn = False
                    DartboardPanel.drawDartboard(screen)
                    buttons = ButtonPanel.drawButtons(screen)
                    DartboardPanel.TOTAL_DARTS = 0
                    InfoPanel.speed = 20
                    DartboardPanel.DARTS = [['N/A', 'no darts thrown yet!']]
                    DartboardPanel.RING_COUNT = [0, 0, 0, 0, 0]
                    DartboardPanel.PERCENTAGES = [0, 0, 0, 0, 0]
                elif buttons[3].collidepoint(click):
                    InfoPanel.speed += 5
                elif buttons[4].collidepoint(click):
                    InfoPanel.speed -= 5
        if dartsOn:
            DartboardPanel.throwDarts(screen)
        InfoPanel.drawInfo(screen)
        p.display.flip()  # update the screen
        clock.tick(InfoPanel.speed)  # FPS of screen updating
    p.quit()  # close display window (and all pygame stuff) after ending loop


# python script to run the main function
if __name__ == "__main__":
    main()