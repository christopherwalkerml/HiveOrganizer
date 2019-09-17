#the menu page parent is the base file for all menu pages.
#the only thing that changes per menu is the destination of "open"/"create" and the button names

from pages.pageparent import pageparent
from pages.objects.menubuttonparent import *
from pages.objects.deletebutton import deletebutton
from pages.scripts.readwritefile import *
from pages.objects.backbutton import *

cell = pygame.image.load(dir + '\images\cell.png').convert_alpha()

class menupageparent(pageparent):

    def __init__(self, directory, buttonname, destpage):
        pageparent.__init__(self)
        self.delbutton = None
        self.selectedbutton = None
        self.directory = directory
        self.buttonname = buttonname
        self.destpage = destpage

    def startup(self):
        choices = []
        if os.stat(dir + self.directory).st_size != 0:  # check to see if the file isn't empty
            file = open(dir + self.directory, 'r')  # load data from file and make schedules
            for lines in file:
                choices.append(eval(lines.strip()))
            file.close()
            s = 0
            for s in range(len(choices)):
                self.buttonlist.append(menubuttonparent(self.win, choices[s][0], s, self.destpage))

            self.buttonlist.append(menubuttonparent(self.win, self.buttonname, s + 1, self.destpage, True)) #this button is the 'create new file' button
        else:
            self.buttonlist.append(menubuttonparent(self.win, self.buttonname, 0, self.destpage, True))

        self.buttonlist.append(backbutton(self.win, 'menupage'))

    def draw(self, mpos):
        if self.fadeout < 225:
            self.finishing()
        else:
            self.win.fill(HIVE)
            self.decorate() #draw the little hexagons
            for b in self.buttonlist:
                b.key = self.key
                b.draw(mpos)
            if self.fadein < 255:
                self.starting(True)
        self.run(mpos)

    def run(self, mpos):
        if self.delbutton is not None:
            self.delbutton.draw() #if the delete button should be drawn, draw it
        if self.isclicked:
            createdelbutton = False
            for b in range(len(self.buttonlist)):
                ishover = self.buttonlist[b].ishovering(mpos)
                if ishover:
                    if ishover.text == 'Delete' and self.buttonlist[b] != self.buttonlist[-2]:
                        if self.delbutton is None:
                            self.selectedbutton = b #if the delete button is clicked on a schedule display, create the delete confirmation button
                            createdelbutton = True
                    break
            if self.delbutton is not None:
                if self.delbutton.ishovering(mpos):
                    del self.buttonlist[self.selectedbutton] #if the delete confirmation button is clicked, delete the schedule, and update the rest
                    lines = readfile(self.directory)
                    file = open(dir + self.directory, 'w')
                    for l in range(len(lines)):
                        for b in self.buttonlist: #only insert the data into the save file that should be there. deleted buttons should be removed
                            if l == b.num:
                                file.write(lines[l] + '\n') #(delete the file that was said to be deleted)
                    file.close()
                    for z in range(len(self.buttonlist) - self.selectedbutton): #if the user clicks anything except the delete confirmation button, it will go away
                        self.buttonlist[self.selectedbutton + z].num -= 1
                    for z in self.buttonlist:
                        z.update() #update the buttons
                self.delbutton = None

            if createdelbutton:
                self.delbutton = deletebutton(self.win, cell, ['Delete?', '(click here to delete)'], (self.buttonlist[self.selectedbutton].rect[1] + (self.buttonlist[self.selectedbutton].rect[3] / 2) - (cell.get_height() / 2)))
        hoverbuttonindex = None
        for b in self.buttonlist:
            ishover = b.ishovering(mpos)
            if ishover:
                if ishover.canhover:
                    hoverbuttonindex = b.num
                    ishover.ishovered = True
                else:
                    ishover.ishovered = False
        file = open('datapass.txt','w')
        file.write(str(hoverbuttonindex))
        file.close()