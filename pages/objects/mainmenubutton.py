#button class
import pygame

class mainmenubutton:

    def __init__(self, win, pos, pic, size):
        self.win = win
        self.pos = pos
        self.pic = pic
        self.size = size
        self.transformedsize = self.size
        self.dest = None

    def ishovering(self, mpos):
        #if the mouse position is within range of the button
        if abs(mpos[0] - self.pos[0]) < self.transformedsize[0] / 2:
            if abs(mpos[1] - self.pos[1]) < self.transformedsize[1] / 2:
                if self.dest is None:
                    return True #if the button has no destination, just return True. This is useful for main.py because if True is returned, it doesnt redirect to a different page
                else:
                    return self #return the button that is being hovered

    def transformpic(self, pic, size, fadepercent, transforming):
        p = pygame.transform.scale(pic, (int(size[0] + ((transforming / 150) * size[0])), int(size[1] + ((transforming / 150) * size[1])))) #transform the button
        self.transformedsize = (p.get_width(), p.get_height())
        p.set_alpha(255 - (fadepercent * 255))
        return p, (self.pos[0] - (self.transformedsize[0] / 2), self.pos[1] - (self.transformedsize[1] / 2)) #return the place it needs to be blitted

    def draw(self, mpos = None):
        p = self.transformpic(self.pic, self.size, 0, 100)
        self.win.blit(p[0], p[1])