#centers the text on the screen
BLACK = (0, 0, 0)
from pages.colour import *

def centertext(text, font, winwid, winhig):   #Center the text in the middle of the screen.
    text = font.render(text, True, BLACK)
    tpos = ((winwid/2) - (text.get_rect().width / 2), (winhig/2) - (text.get_rect().height / 2))   #gets half the height, half the width, and takes away half the
    return tpos  

def centerboxtext(text, font, rect):
    text = font.render(text, True, BLACK)
    tpos = ((rect[2] / 2) - (text.get_rect().width / 2) + rect[0], (rect[3] / 2) - (text.get_rect().height / 2) + rect[1])
    return tpos