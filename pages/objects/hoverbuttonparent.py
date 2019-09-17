#this button is a simple button that blits an image, and returns when it's being hovered

import pygame

class hoverbutton:

    def __init__(self, win, pos, pic, dest):
        self.win = win
        self.pos = pos
        self.pic = pic
        self.dest = dest
        self.canhover = True

    def draw(self, mpos):
        if self.ishovering(mpos):
            self.win.blit(pygame.transform.scale(self.pic, (self.pic.get_width() + 4, self.pic.get_height() + 4)), (self.pos[0] - 3, self.pos[1] - 6)) #if the button is being hovered, grow in size
        else:
            self.win.blit(self.pic, self.pos)

    def ishovering(self, mpos):
        if self.pos[0] < mpos[0] < self.pos[0] + self.pic.get_width():
            if self.pos[1] < mpos[1] < self.pos[1] + self.pic.get_height():
                if self.dest is None:
                    return True #if the button has no destination, just return True. This is useful for main.py because if True is returned, it doesnt redirect to a different page
                else:
                    return self #return the button that is being hovered