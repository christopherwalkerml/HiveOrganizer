#this button is very minimal. is tests if you're hovering over it, it draws itself as a rectangle, and can draw text

from pages.scripts.centertext import *
import pygame

class mainbutton:

    def __init__(self, win, text, textsize, rect, canhover = True, dest = None, drawtype = 'rect'):
        self.win = win
        self.text = text[0] #text = ('str', centered)
        self.ctext = text[1]
        self.rect = rect
        self.canhover = canhover
        self.ishovered = False
        self.dest = dest
        self.textsize = textsize
        self.sizechange = 0
        self.drawtype = drawtype
        self.font = pygame.font.Font(dir + '\pages\Font.ttf', self.textsize)
        while self.font.render(self.text, True, BLACK).get_rect().width > self.rect[2]:
            self.textsize -= 2
            self.font = pygame.font.Font(dir + '\pages\Font.ttf', self.textsize)

    def __repr__(self):
        return str([
            self.text,
            self.rect,
            self.dest
        ])

    def ishovering(self, mpos):
        # if the mouse position is within range of the button
        if self.canhover:
            if self.rect[0] < mpos[0] < self.rect[0] + self.rect[2]:
                if self.rect[1] < mpos[1] < self.rect[1] + self.rect[3]:
                    return self

    def drawrect(self, mpos):
        drawcol = HIVEWALL
        if self.drawtype == 'rect': #if the drawtype is rect, it will surround the text with a rectangle
            if self.canhover:
                if self.ishovering(mpos):
                    pygame.draw.rect(self.win, HIVEWALL, self.rect) #if the button is being hovered, invert the colours; Make the text HIVE, and the rect HIVEWALL
                    drawcol = HIVE
            else:
                pygame.draw.rect(self.win, HIVE, self.rect)
            pygame.draw.rect(self.win, HIVEWALL, self.rect, 3)

        elif self.drawtype == 'line': #if the drawtype is a line, it will underline the text
            if self.sizechange != 0:
                self.font = pygame.font.Font(dir + '\pages\Font.ttf', self.textsize)
            self.sizechange = 0
            if self.canhover:
                if self.ishovering(mpos):
                    self.sizechange = self.rect[2] / 10
                    self.font = pygame.font.Font(dir + '\pages\Font.ttf', self.textsize + 8)
            pygame.draw.line(self.win, HIVEWALL, (self.rect[0] - self.sizechange, self.rect[1] + self.rect[3] + (self.sizechange / 3)),
                                                 (self.rect[0] + self.rect[2] + self.sizechange, self.rect[1] + self.rect[3] + (self.sizechange / 3)), int(3 + (self.sizechange / 10)))
        if self.ctext == False: #if there is no draw type, no exterior will be drawn. just text
            self.win.blit(self.font.render(self.text, False, drawcol), (self.rect[0] + 10, self.rect[1]))  # if the text isnt being centered
        else:
            tpos = centerboxtext(self.text, self.font, self.rect)
            if type(self.ctext) == tuple:
                self.win.blit(self.font.render(self.text, False, drawcol), (tpos[0], self.rect[1]))  # if its not being completely centered, just center the x, and put the y where the rect is
            else:
                self.win.blit(self.font.render(self.text, False, drawcol), tpos)  # center the text completely