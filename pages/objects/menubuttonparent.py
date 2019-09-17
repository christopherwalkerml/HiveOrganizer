#this is themenu button parent. all menu buttons are roughly the same
#the only thing that changes is the destination of the button

from pages.objects.mainbutton import *
from pages.objects.inputobject import *

font = pygame.font.Font(dir + '\pages\Font.ttf', 60)

class menubuttonparent(mainbutton):

    def __init__(self, win, text, num, dest, newsched = False):
        self.winwid = win.get_width()
        self.winhig = win.get_height()
        self.rect = ((self.winwid / 2) - (self.winwid / 8), 80 + (num * 160), self.winwid / 4, 110)  # create the rect for the button
        self.input = inputobj(win, (self.rect[0], self.rect[1], self.rect[2], 60), font, text, 'center')
        mainbutton.__init__(self, win, ('', (True, False)), 60, self.rect, False, dest)
        self.num = num
        self.buttonlist = []
        self.canhover = False
        self.key = None
        prect = (self.rect[0] + self.rect[2] - (self.rect[2] - (self.rect[2] / 1.2)) - 10,
                 self.rect[1] + self.rect[3] - (self.rect[3] - (self.rect[3] / 1.5)) - 10, #create the rectangle for the open button
                 (self.rect[2] - (self.rect[2] / 1.2)), (self.rect[3] - (self.rect[3] / 1.5)))
        if newsched == False:
            self.buttonlist.append(mainbutton(win, ('Open', True), 26, prect, True, self.dest))
            self.buttonlist.append(mainbutton(win, ('Delete', True), 26, (self.rect[0] + 10, prect[1], prect[2], prect[3])))
        else:
            self.buttonlist.append(mainbutton(win, ('Create', True), 26, prect, True, self.dest))

    def ishovering(self, mpos):
        for b in self.buttonlist:
            # if the mouse position is within range of the button
            if b.canhover:
                if b.rect[0] < mpos[0] < b.rect[0] + b.rect[2]:
                    if b.rect[1] < mpos[1] < b.rect[1] + b.rect[3]:
                        return b

    def draw(self, mpos):
        self.drawrect(mpos)
        self.input.draw(mpos, self.key)
        for b in self.buttonlist:
            b.drawrect(mpos)

    def update(self):
        self.rect = ((self.winwid / 2) - (self.winwid / 8), 80 + (self.num * 160), self.winwid / 4, 110)  # create the rect for the button
        prect = (self.rect[0] + self.rect[2] - (self.rect[2] - (self.rect[2] / 1.2)) - 10,
                 self.rect[1] + self.rect[3] - (self.rect[3] - (self.rect[3] / 1.5)) - 10, # create the rectangle for the open button
                 (self.rect[2] - (self.rect[2] / 1.2)), (self.rect[3] - (self.rect[3] / 1.5)))
        self.buttonlist[0].rect = prect
        if len(self.buttonlist) == 2:
            self.buttonlist[1].rect = (self.rect[0] + 10, prect[1], prect[2], prect[3]) #the delete button cannot be updated if its the 'create new schedule' button, as it cannot be deleted
        self.input.rect = (self.rect[0], self.rect[1], self.rect[2], 60)