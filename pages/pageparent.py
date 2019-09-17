#this is the parent for all sub-pages (not the menu). It contains the default layout of the pages

import pygame
from random import randrange
from math import cos
from pages.colour import *
from pages.objects.homebutton import homebutton

hivepng = pygame.image.load(dir+'\images\comb.png').convert_alpha()
cell = pygame.image.load(dir+'\images\cell.jpg').convert()
cell = pygame.transform.scale(cell, (32, int((cell.get_height() / cell.get_width()) * 32)))

class pageparent:

    def __init__(self):
        self.fadein = 0
        self.fadeout = 0
        self.win = None
        self.winwid = 0
        self.winhig = 0
        self.buttonlist = []
        self.decolist = []
        self.decocounter = 0
        self.isclicked = False
        self.key = None

    def starting(self, button): #the button variable is if the page requires a home button
        self.fadein += 5
        if self.fadein == 5 and button:
            self.buttonlist.append(homebutton(self.win, (self.winwid - (hivepng.get_width() / 12), (hivepng.get_height() / 12)),
                                              hivepng, (hivepng.get_width() / 12, hivepng.get_height() / 12)))
                                              #add the button to the buttonlist on startup
        fadesurface = pygame.Surface((self.winwid, self.winhig))  # make a surface called fadesurface
        fadesurface.fill(HIVE)  # make the fade surface HIVE colour
        fadesurface.set_alpha(255 - self.fadein)
        self.win.blit(fadesurface, (0, 0))

    def finishing(self):
        self.fadeout += 5
        fadesurface = pygame.Surface((self.winwid, self.winhig))  # make a surface called fadesurface
        fadesurface.fill(HIVE)  # make the fade surface HIVE colour
        fadesurface.set_alpha(self.fadeout)
        self.win.blit(fadesurface, (0, 0))

    def startup(self):
        self.draw((0, 0))

    def click(self, mpos):  # if the mouse clicks a button, return the button's destination page
        for b in self.buttonlist:
            bhover = b.ishovering(mpos)
            if bhover is not None:
                if bhover == True:
                    return bhover
                else:
                    return bhover.dest
        else:
            return None

    def draw(self, mpos):
        if self.fadeout < 225:
            self.finishing()
        else:
            self.win.fill(HIVE)
            self.decorate() #draw the little hexagons
            for b in self.buttonlist:
                b.draw(mpos)
            if self.fadein < 255:
                self.starting(True)

    def decorate(self):
        if randrange(8) == 0:
            if len(self.decolist) < 75:
                self.decolist.append(deco(self.win, self.winwid, self.winhig))  # add a decoration item to the deco list if there arent over 50 already
        dellist = []
        for d in range(len(self.decolist)):
            if self.decolist[d].cosine <= 0:
                dellist.append(d)  # if the deco item is done its cycle, delete it
            else:
                self.decolist[d].draw()  # draw the deco item
        for d in dellist:
            del self.decolist[d]

class deco:

    def __init__(self, win, winwid, winhig):
        self.win = win
        self.pos = (randrange(0, winwid), randrange(0, winhig))
        self.fade = 0
        self.cosine = 0.005
        self.sinedir = 0.005
        self.surf = cell

    def draw(self):
        self.cosine += self.sinedir
        if self.cosine >= 1:
            self.sinedir = -0.005
        self.surf.set_alpha(255 - (cos(self.cosine) * 255))
        self.win.blit(self.surf, self.pos)