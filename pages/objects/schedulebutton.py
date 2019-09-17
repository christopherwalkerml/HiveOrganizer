#these button classes will display all the schedule information
#the first button will display all the names of the schedules and give an option to open them
#the second button will display the percent completed of the scheduled task, and the name of the task
#the third button
#its not really a button, but more of a display icon

from pages.objects.menubuttonparent import *

arrow = pygame.image.load(dir + r'\images\arrow.png')
plus = pygame.image.load(dir + r'\images\plus.png')
minus = pygame.image.load(dir + r'\images\minus.png')
font = pygame.font.Font(dir+'\pages\Font.ttf', 36)
play = pygame.image.load(dir + r'\images\play.png')
pause = pygame.image.load(dir + r'\images\pause.png')

class schedulebutton(mainbutton):

    def __init__(self, win, task):
        self.win = win
        self.winwid = self.win.get_width()
        self.winhig = self.win.get_height()
        self.task = task
        self.rect = ((self.winwid / 2) - (self.winwid / 6), 160 + (self.task.num * 160), self.winwid / 3, 110)  # create the rect for the button
        mainbutton.__init__(self, win, (task.name, False), 32, self.rect, False)
        #Stored values from the task
        # task.name,
        # task.duration,
        # task.isdone,
        # task.num,
        # task.telapsed,
        # task.worktype
        self.num = task.num
        self.buttonlist = []
        self.iscurrent = False
        prect = (self.rect[0] + self.rect[2] - (self.rect[2] - (self.rect[2] / 1.2)) - 10,
                 self.rect[1] + self.rect[3] - (self.rect[3] - (self.rect[3] / 1.5)) - 10,
                 # create the rectangle for the open button
                 (self.rect[2] - (self.rect[2] / 1.2)), (self.rect[3] - (self.rect[3] / 1.5)))
        self.buttonlist.append(mainbutton(win, ('Edit', True), 26, (self.rect[0] + 10, prect[1], prect[2], prect[3]), True))

    def draw(self, mpos): #draw the displays with their text, percentage bar, and more
        self.drawrect(mpos)
        for b in self.buttonlist:
            b.drawrect(mpos)
        srectwid = self.rect[2] - (self.rect[2] / 2) #get the locations and sizes for the percentage rectangle
        srecthig = self.rect[3] - (self.rect[3] / 1.5)
        srect = (self.rect[0] + self.rect[2] - srectwid - 10, self.rect[1] + self.rect[3] - srecthig - 10, srectwid, srecthig) #create coordinates for the percentage rectangle
        if int(self.task.percent) != 0:
            if self.task.percent < 100:
                pygame.draw.rect(self.win, LGREEN, (srect[0], srect[1], srect[2] * (self.task.percent / 100), srect[3]))
            else:
                pygame.draw.rect(self.win, LRED, srect)
        pygame.draw.rect(self.win, HIVEWALL, srect, 2)  # draw the percentage rectangle
        tpos = centerboxtext(str(int(self.task.telapsed // 60)) + '/' + str(int(self.task.duration // 60)) + 'mins', font, srect)
        self.win.blit(font.render(str(int(self.task.telapsed // 60)) + '/' + str(int(self.task.duration // 60)) + 'mins', False, HIVEWALL), tpos)
        if self.task.sched.curtask == self.task:
            if self.task.sched.active:
                self.win.blit(pygame.transform.scale(play, (int(srect[3] - 8), int(srect[3] - 4))), (int(srect[0] - int(srect[3] - 4)), int(srect[1] + 2))) #draw the play / pause button if it is the current task
            else:
                self.win.blit(pygame.transform.scale(pause, (int(srect[3] - 10), int(srect[3] - 4))), (int(srect[0] - int(srect[3] - 6)), int(srect[1] + 2)))

    def update(self):
        self.num = self.task.num
        self.rect = ((self.winwid / 2) - (self.winwid / 6), 160 + (self.task.num * 160), self.winwid / 3, 110)
        prect = (self.rect[0] + self.rect[2] - (self.rect[2] - (self.rect[2] / 1.2)) - 10,
                 self.rect[1] + self.rect[3] - (self.rect[3] - (self.rect[3] / 1.5)) - 10, # create the rectangle for the open button
                 (self.rect[2] - (self.rect[2] / 1.2)), (self.rect[3] - (self.rect[3] / 1.5)))
        self.buttonlist[0].rect = (self.rect[0] + 10, prect[1], prect[2], prect[3])

class scheduleaddrembutton:

    def __init__(self, win, num, addorrem):
        self.win = win
        self.winwid = win.get_width()
        self.winhig = win.get_height()
        self.num = num
        self.addorrem = addorrem #variable to determine type of button (add or remove)
        self.surf = pygame.Surface((64, 48))
        self.surf.fill(WHITE)
        self.surf.set_colorkey(WHITE)
        self.dest = None
        if addorrem == 'add':
            self.pos = ((self.winwid / 2) + (self.winwid / 6) + 8, 114 + (num * 160)) #add the "add new task here" button. The three lines after those are for "remove task" buttons
            self.surf.blit(pygame.transform.scale(arrow, (int(arrow.get_width() / plus.get_width() * 32), int(arrow.get_height() / plus.get_width() * 32))), (0, 0))
            self.surf.blit(pygame.transform.scale(plus, (int(plus.get_width() / plus.get_width() * 32), int(plus.get_height() / plus.get_width() * 32))), (25, (self.surf.get_height() / 2) - 19))
        else:
            self.pos = ((self.winwid / 2) - (self.winwid / 6) - self.surf.get_width() - 8, 164 + (num * 160) + ((110 / 2) - (self.surf.get_height() / 2)))
            self.surf.blit(pygame.transform.scale(minus, (int(minus.get_width() / minus.get_width() * 32), int(minus.get_height() / minus.get_width() * 32))), (0, (self.surf.get_height() / 2) - 19))
            self.surf.blit(pygame.transform.rotate(pygame.transform.scale(arrow, (int(arrow.get_width() / minus.get_width() * 32), int(arrow.get_height() / minus.get_width() * 32))), 180), (32, 0))

    def draw(self, mpos = None):
        if self.ishovering(mpos):
            self.win.blit(pygame.transform.scale(self.surf, (80, 60)), (self.pos[0] - 8, self.pos[1] - 4))
        else:
            self.win.blit(self.surf, self.pos)

    def update(self):
        if self.addorrem == 'add':
            self.pos = ((self.winwid / 2) + (self.winwid / 6) + 8, 114 + (self.num * 160)) #update the positions of the add and rem buttons when a new task is added
        else:
            self.pos = ((self.winwid / 2) - (self.winwid / 6) - self.surf.get_width() - 8, 164 + (self.num * 160) + ((110 / 2) - (self.surf.get_height() / 2)))

    def ishovering(self, mpos):
        if self.pos[0] < mpos[0] < self.pos[0] + self.surf.get_width():
            if self.pos[1] < mpos[1] < self.pos[1] + self.surf.get_height():
                if self.dest is None:
                    return True #if the button has no destination, just return True. This is useful for main.py because if True is returned, it doesnt redirect to a different page
                else:
                    return self #return the button that is being hovered