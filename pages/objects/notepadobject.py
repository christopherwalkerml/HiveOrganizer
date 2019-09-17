#this object is responsible for all of the notepad file functionality. Minimizing, expanding, editing, moving, drawing, etc

from pages.colour import *
from pages.objects.hoverbuttonparent import *
from pages.scripts.centertext import *

xpng = pygame.image.load(dir + '\images\close.png')
xpng.set_colorkey(WHITE)
xpng = pygame.transform.scale(xpng, (32, 32))
pluspng = pygame.image.load(dir + '\images\plus.png')
pluspng.set_colorkey(WHITE)
pluspng = pygame.transform.scale(pluspng, (32, 32))
minuspng = pygame.image.load(dir + '\images\minus.png')
minuspng.set_colorkey(WHITE)
minuspng = pygame.transform.scale(minuspng, (32, 32))

font = pygame.font.Font(dir+'\pages\Font.ttf', 32)

class notepadobject:

    def __init__(self, win, pos, name, content, isopen):
        self.win = win
        self.pos = pos
        self.name = name
        self.content = content
        self.isopen = isopen
        self.minsize = 160
        self.width = self.minsize
        self.buttonlist = []
        self.isclicked = False
        self.clickpos = [0, 0]
        self.delete = False
        self.canhover = True
        self.buttonlist.append(hoverbutton(win, (self.pos[0], self.pos[1] - 32), xpng, None))
        self.buttonlist.append(hoverbutton(win, (self.pos[0] + self.width - 32, self.pos[1] - 32), minuspng, None))
        self.buttonlist.append(hoverbutton(win, (self.pos[0] + self.width - 32, self.pos[1] - 32), pluspng, None))

    def __repr__(self):
        return str([
            self.pos,
            self.name,
            self.content,
            self.isopen
        ])

    def draw(self, mpos):
        self.buttonlist[0].draw(mpos)
        if self.isopen:
            self.buttonlist[1].draw(mpos)
            self.buttonlist[1].canhover = True
            self.buttonlist[2].canhover = False
        else:
            self.buttonlist[2].draw(mpos)
            self.buttonlist[1].canhover = False
            self.buttonlist[2].canhover = True
        tpos = centerboxtext(self.name, font, (self.pos[0], self.pos[1], self.width, 3))
        self.win.blit(font.render(self.name, False, HIVEWALL), (tpos[0], self.pos[1] - 32))
        pygame.draw.rect(self.win, HIVEWALL, (self.pos[0], self.pos[1], self.width, 3))
        self.run(mpos)

    def run(self, mpos):
        if pygame.mouse.get_pressed()[0]:
            if self.isclicked == False:
                for b in range(len(self.buttonlist)):
                    if self.buttonlist[b].ishovering(mpos):
                        if b == 0:
                            self.delete = True
                            return
                        else:
                            if self.buttonlist[b].canhover:
                                if b == 1:
                                    self.isopen = False
                                    break
                                elif b == 2:
                                    self.isopen = True
                                    break
            if self.isclicked:
                self.pos = (self.pos[0] - (self.clickpos[0] - mpos[0]), self.pos[1] - (self.clickpos[1] - mpos[1])) #if the mouse is clicked and moved on top of the file, move the file where the mouse goes
                self.update()
            if self.pos[0] < mpos[0] < self.pos[0] + self.width:
                if self.pos[1] - 32 < mpos[1] < self.pos[1] + 3:
                    self.isclicked = True
                    self.clickpos = mpos
        else:
            self.isclicked = False

    def ishovering(self, mpos):
        for b in self.buttonlist:
            hovering = b.ishovering(mpos)
            if hovering:
                return hovering

    def update(self):
        self.buttonlist[0].pos = (self.pos[0], self.pos[1] - 32)
        self.buttonlist[1].pos = (self.pos[0] + self.width - 32, self.pos[1] - 32) #if the file is moved, the location of the buttons must be moved as well
        self.buttonlist[2].pos = (self.pos[0] + self.width - 32, self.pos[1] - 32)