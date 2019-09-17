#this button asks the user if they are cert ain that they wish to dele the chosen display

import pygame
from pages.colour import *

font32 = pygame.font.Font(dir+'\pages\Font.ttf', 32)
font16 = pygame.font.Font(dir+'\pages\Font.ttf', 16)

class deletebutton:

    def __init__(self, win, pic, text, ypos):
        self.win = win
        self.pic = pic
        self.text = text
        self.ypos = ypos
        self.xpos = 0

    def draw(self):
        self. xpos = (self.win.get_width() / 2) - (self.pic.get_width() / 2)
        self.win.blit(self.pic, (self.xpos, self.ypos))
        textsize = font32.render(self.text[0], True, BLACK)
        self.win.blit(font32.render(self.text[0], False, HIVEWALL), ((self.xpos + (self.pic.get_width() / 2) - (textsize.get_rect().width / 2)), (self.ypos + 64)))
        textsize = font16.render(self.text[1], True, BLACK)
        self.win.blit(font16.render(self.text[1], False, HIVEWALL), ((self.xpos + (self.pic.get_width() / 2) - (textsize.get_rect().width / 2)), (self.ypos + 104)))

    def ishovering(self, mpos):
        #if the mouse position is within range of the button
        if self.xpos < mpos[0] < self.xpos + self.pic.get_width():
            if self.ypos < mpos[1] < self.ypos + self.pic.get_height():
                return True