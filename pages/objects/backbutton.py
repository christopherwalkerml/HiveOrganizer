#creates the back button

import pygame
from pages.scripts.centertext import *

arrow = pygame.image.load(dir + r'\images\arrow.png')
minus = pygame.image.load(dir + r'\images\minus.png')
font = pygame.font.Font(dir+'\pages\Font.ttf', 42)

class backbutton:

    def __init__(self, win, dest):
        self.win = win
        self.dest = dest
        self.surf = pygame.Surface((124, 64))
        self.pos = [10, 10]
        self.canhover = False
        self.num = -1
        self.surf.fill(WHITE)
        self.surf.set_colorkey(WHITE)
        self.surf.blit(pygame.transform.scale(arrow, (int(arrow.get_width() / minus.get_width() * 48), int(arrow.get_height() / minus.get_width() * 48))), (0, 0))
        tpos = centerboxtext('Back', font, (0, 0, self.surf.get_width(), self.surf.get_height()))
        self.surf.blit(font.render('Back', False, HIVEWALL), (tpos[0] + 20, tpos[1]))

    def draw(self, mpos):
        if self.ishovering(mpos):
            self.win.blit(pygame.transform.scale(self.surf,(int(self.surf.get_width() * 1.2), int(self.surf.get_height() * 1.2))), (4, 4))
        else:
            self.win.blit(self.surf, (10, 10))

    def ishovering(self, mpos):
        if self.pos[0] < mpos[0] < self.pos[0] + self.surf.get_width():
            if self.pos[1] < mpos[1] < self.pos[1] + self.surf.get_height():
                if self.dest is None:
                    return True #if the button has no destination, just return True. This is useful for main.py because if True is returned, it doesnt redirect to a different page
                else:
                    return self #return the button that is being hovered

    def update(self):
        pass