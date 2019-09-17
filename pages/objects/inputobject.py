#this object will, when clicked, accept any input in the form of a keyboard, and return the key clicked. When esc is clicked, it will stop accepting input
#if the input object is a one-liner, hitting enter will also exit the input object

import pygame
from pages.scripts.centertext import *

class inputobj:

    def __init__(self, win, rect, font, text, align):
        self.win = win
        self.rect = rect
        self.text = text
        self.font = font
        self.align = align
        if type(self.text) == list:
            self.texttype = 'lines'
        else:
            self.texttype = 'line'
        self.clicked = False
        self.canwrite = False
        self.writeindex = -1
        textsize = self.font.get_height()
        while self.font.render(self.text, True, BLACK).get_rect().width > self.rect[2]:
            textsize -= 2
            self.font = pygame.font.Font(dir + '\pages\Font.ttf', textsize)

    def isclicked(self, mpos):
        if pygame.mouse.get_pressed()[0] and self.clicked == False:
            self.clicked = True
            if self.rect[0] < mpos[0] < self.rect[0] + self.rect[2]:
                if self.rect[1] < mpos[1] < self.rect[1] + self.rect[3]:
                    self.canwrite = True
                    return
            self.canwrite = False
        else:
            self.clicked = False

    def draw(self, mpos, key):
        self.isclicked(mpos)
        if self.texttype == 'line':
            if self.align == 'left':
                self.win.blit(self.font.render(self.text, False, HIVEWALL, (self.rect[0] + 3, self.rect[1] + 3)))
            elif self.align == 'center':
                self.win.blit(self.font.render(self.text, False, HIVEWALL), centerboxtext(self.text, self.font, self.rect))
        elif self.texttype == 'lines':
            if self.align == 'left':
                for l in range(len(self.text)):
                    self.win.blit(self.font.render(self.text[l], False, HIVEWALL, (self.rect[0] + 3, self.rect[1] + 3 + (l * (self.font.get_height() + 4)))))
        # depending on the key entered, change the text in the input object
        if self.canwrite:
            if key is not None:
                for k in key:
                    if k == 32:
                        print('space')
                    elif k == 13:
                        print('enter')
                    elif k == 8:
                        print('backspace')
                    elif 97 <= k <= 122:
                        print(chr(k))