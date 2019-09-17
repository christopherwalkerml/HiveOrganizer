#this page displays all the information about the schedule

from scheduler import schedule
from pages.pageparent import *
from pages.objects.schedulebutton import *
from pages.scripts.centertext import *
from pages.scripts.readwritefile import *
from pages.objects.backbutton import backbutton

afont = pygame.font.Font(dir + '\pages\Font.ttf', 60)
bfont = pygame.font.Font(dir + '\pages\Font.ttf', 42)
pause = pygame.image.load(dir + '\images\pause.png').convert_alpha()
play = pygame.image.load(dir + '\images\play.png').convert_alpha()

class schedulepage(pageparent):

    def __init__(self):
        pageparent.__init__(self)
        self.sched = None
        self.addbuttonlist = []
        self.rembuttonlist = []
        self.displaylist = []
        self.ppbutton = None
        self.keydown = None

    def startup(self):
        schedules = []
        if os.stat(dir + '\scheduler\sdata.txt').st_size != 0:  # check to see if the file isn't empty
            file = open(dir + '\scheduler\sdata.txt', 'r')  # load data from file and make schedules
            for lines in file:
                schedules.append(eval(lines.strip()))
            file.close()

        findex = open('datapass.txt', 'r') #file index
        index = findex.readline().strip()
        if index is not None and len(schedules) > int(index): #import the index of the button that was pressed so it can load the proper schedule
            importsched = schedules[int(index)]
        else:
            importsched = None

        if importsched is not None:
            self.sched = schedule.schedule(importsched[0]) #add all the data from sdata to the schedule as buttons and tasks
            i = 0
            for i in range(len(importsched[2])):
                self.sched.addtask(importsched[2][i][0], importsched[2][i][1], importsched[2][i][2], importsched[2][i][3], importsched[2][i][4], importsched[2][i][5])
                self.displaylist.append(schedulebutton(self.win, self.sched.tasklist[-1]))
                self.addbuttonlist.append(scheduleaddrembutton(self.win, i, 'add'))
                self.rembuttonlist.append(scheduleaddrembutton(self.win, i, 'rem')) #create the add and remove buttons for each task
            if i != 0:
                self.addbuttonlist.append(scheduleaddrembutton(self.win, i + 1, 'add'))
            else:
                self.addbuttonlist.append(scheduleaddrembutton(self.win, 0, 'add'))
        else:
            self.sched = schedule.schedule('Unnamed Schedule') #if a new schedule was created, read all the data from the sdata file, and update it with the new schedule
            lines = readfile('\scheduler\sdata.txt')
            lines.append(self.sched.__repr__())
            writefile('\scheduler\sdata.txt', lines)
            self.addbuttonlist.append(scheduleaddrembutton(self.win, 0, 'add')) #give the add task button to the new schedule, as it will require it to add its first task
        self.buttonlist.append(backbutton(self.win, 'schedulemenupage'))
        self.sched.update()

    def draw(self, mpos):
        if self.fadeout < 225:
            self.finishing()
        else:
            self.win.fill(HIVE)
            self.decorate() #draw the little hexagons
            ct = centertext(self.sched.name, afont, self.winwid, self.winhig)
            self.win.blit(afont.render(self.sched.name, False, HIVEWALL), (ct[0], 8))
            ct = centertext('Projected Completion Time:', bfont, self.winwid, self.winhig)
            self.win.blit(bfont.render('Projected Completion Time:', False, HIVEWALL), (ct[0], 70))
            eta = self.sched.eta()
            if len(str(eta[1])) == 1:
                eta = str(eta[0]) + ':' + '0' + str(eta[1])
            else:
                eta = str(eta[0]) + ':' + str(eta[1])
            ct = centertext(eta, bfont, self.winwid, self.winhig)
            self.win.blit(bfont.render(eta, False, HIVEWALL), (ct[0], 116))
            self.run(mpos)
            for b in self.buttonlist:
                b.draw(mpos)
            for b in self.addbuttonlist:
                b.draw(mpos)
            for b in self.rembuttonlist: #draw everything
                b.draw(mpos)
            for b in self.displaylist:
                b.draw(mpos)
            if self.fadein < 255:
                self.starting(True)

    def run(self, mpos):
        self.sched.run()
        if self.isclicked:
            for b in self.addbuttonlist:
                if b.ishovering(mpos):
                    bnum = b.num
                    if bnum == self.addbuttonlist[-1].num:
                        self.sched.addtask('empty', 20, False, bnum, 0, 'work')
                        self.displaylist.append(schedulebutton(self.win, self.sched.tasklist[-1]))
                        self.addbuttonlist.append(scheduleaddrembutton(self.win, bnum + 1, 'add')) #if the add button is the last add button, append a new display, and add new add and remove buttons
                        self.rembuttonlist.append(scheduleaddrembutton(self.win, bnum, 'rem'))
                    else:
                        self.sched.addtask('empty', 20, False, bnum, 0, 'work')
                        self.displaylist.insert(bnum, schedulebutton(self.win, self.sched.tasklist[bnum]))
                        self.addbuttonlist.insert(bnum, scheduleaddrembutton(self.win, bnum, 'add')) #if the add button is in the middle of the pack, isnert it, and insert add and remove buttons
                        self.rembuttonlist.insert(bnum, scheduleaddrembutton(self.win, bnum, 'rem'))
                        self.updatenum(1, bnum)
                    self.sched.save()
                    break
            for b in self.rembuttonlist:
                if b.ishovering(mpos):
                    bnum = b.num
                    self.sched.remtask(bnum)
                    del self.displaylist[bnum]
                    del self.addbuttonlist[bnum]
                    del self.rembuttonlist[bnum]
                    self.updatenum(-1, bnum)
                    break
            for z in self.displaylist:
                z.update()
            for z in self.addbuttonlist: #update the rects and positions of the buttons and displays if the schedule changes
                z.update()
            for z in self.rembuttonlist:
                z.update()

        if self.keydown == 32:
            self.sched.active = not self.sched.active
            self.keydown = None
        if self.keydown == 13:
            self.keydown = None
            self.sched.startnexttask()

    def updatenum(self, val, bnum):
        if val == 1:
            num = 1
        else:
            num = 0
        for z in range(len(self.addbuttonlist) - (bnum + num)):
            self.addbuttonlist[bnum + z + num].num -= -val
        for z in range(len(self.rembuttonlist) - (bnum + num)):  # update all the numbers of the other buttons
            self.rembuttonlist[bnum + z + num].num -= -val
        for z in range(len(self.displaylist) - (bnum + num)):  # the +num is sometimes used here because they cannot include themselves when adding nums
            self.displaylist[bnum + z + num].num -= -val