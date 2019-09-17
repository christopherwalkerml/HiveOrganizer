#this is the menu page. This is what runs the menu.
#no parameters are allowed.

#helper scripts
from pages.scripts.updatecentertime import *
from pages.pageparent import *
from pages.scripts.gettime import *
from pages.scripts.sortbuttonlist import *
from pages.objects.menubutton import *
from pages.colour import *

#import the images for the program
hivepng = pygame.image.load(dir+'\images\comb.png').convert_alpha()
combpng = pygame.image.load(dir+'\images\cell.png').convert_alpha()
todopng = pygame.image.load(dir+r'\images\todo.png').convert()
todopng.set_colorkey(WHITE) #this makes list a fade-able object
notepadpng = pygame.image.load(dir+r'\images\notepad.png').convert()
notepadpng.set_colorkey(WHITE)
schedulepng = pygame.image.load(dir+r'\images\schedule.png').convert()
schedulepng.set_colorkey(WHITE)
font = pygame.font.Font(dir+'\pages\Font.ttf', 42)

class menupage(pageparent):

    def __init__(self):
        pageparent.__init__(self)
        self.transformin = 0
        self.lastcurtime = None
        self.lastcursecs = None
        self.hivepngwidth = 0
        self.hivepngheight = 0
        self.size = 0
        self.sizeto = 0

    def draw(self, mpos):
        if self.fadeout < 225:
            self.finishing()
        else:
            if self.transformin < 151:
                if self.transformin < 150:
                    if self.transformin == 0:
                        self.size = 100
                        self.sizeto = 50
                    elif self.transformin == 60:
                        self.size = 50
                        self.sizeto = 90

                    self.win.fill(HIVE)
                    self.size -= ((self.size - self.sizeto) * 0.05)  # shrink the logo
                    self.hivepngwidth = int(hivepng.get_width() * (self.size / 100))  # set the custom width and height for the into animation
                    self.hivepngheight = int(hivepng.get_height() * (self.size / 100))
                    p = pygame.transform.scale(hivepng, (self.hivepngwidth, self.hivepngheight))  # transform the logo
                    self.win.blit(p, ((self.winwid / 2) - (self.hivepngwidth / 2), (self.winhig / 2) - (self.hivepngheight / 2)))  # blit it with proper centering

                else:
                    cellsize = (combpng.get_width() * 0.89, combpng.get_height() * 0.89)
                    self.buttonlist = [  # pygame window, position of button, button picture, size of picture, click destination, second picture, size of second picture, [Title, info]
                        menubutton(self.win, (((self.winwid / 2) - 72), (self.winhig / 2) - 125), combpng, cellsize, 'schedulemenupage', schedulepng, (schedulepng.get_width() / 5, schedulepng.get_height() / 5),
                                   ['Schedule', 'make schedules that', 'update themselves']),
                        menubutton(self.win, (((self.winwid / 2) + 72), (self.winhig / 2) - 125), combpng, cellsize, 'notepadmenupage', notepadpng, (notepadpng.get_width() / 5, notepadpng.get_height() / 5),
                                   ['Notepad', 'write notes down.', 'just a notepad']),
                        menubutton(self.win, (((self.winwid / 2) + 144), (self.winhig / 2)), combpng, cellsize, 'todomenupage', todopng, (todopng.get_width() / 5, todopng.get_height() / 5),
                                   ['Todo List', 'create todo lists']),
                        menubutton(self.win, (((self.winwid / 2) + 72), (self.winhig / 2) + 125), combpng, cellsize, None, todopng, (todopng.get_width() / 5, todopng.get_height() / 5), ['Placeholder', 'placeholder text']),
                        menubutton(self.win, (((self.winwid / 2) - 72), (self.winhig / 2) + 125), combpng, cellsize, None, todopng, (todopng.get_width() / 5, todopng.get_height() / 5), ['Placeholder', 'placeholder text']),
                        menubutton(self.win, (((self.winwid / 2) - 144), (self.winhig / 2)), combpng, cellsize, None, todopng, (todopng.get_width() / 5, todopng.get_height() / 5), ['Placeholder', 'placeholder text'])
                    ]
                self.transformin += 1
            else:
                self.win.fill(HIVE)
                p = pygame.transform.scale(hivepng, (self.hivepngwidth, self.hivepngheight)) #transform the logo
                self.win.blit(p, (int((self.winwid / 2) - (self.hivepngwidth / 2)), int((self.winhig / 2) - (self.hivepngheight / 2)))) #blit it with proper centering
                curtime = gettime() #make a variable for current time.
                cursecs = time.time()
                if cursecs != self.lastcursecs: #update the time display every second
                    self.lastcurtime = curtime
                    self.lastcursecs = cursecs
                    center = updatecenter(curtime, self.winwid, self.winhig, font)
                    timedisplay, formattedtime, centertime, centerampm = center[0], center[1], center[2], center[3]
                self.win.blit(font.render(timedisplay, False, HIVEWALL), centertime) #display the time and am/pm
                self.win.blit(font.render(formattedtime[-2::], False, HIVEWALL), centerampm) #display am/pm centered

                btop = None
                blist = sortbuttonsize(self.buttonlist) #this sorts the buttonlist so that the biggest button is drawn last
                for b in blist:
                    if blist[-1].faded == False: #this fades all the buttons in and it looks cool
                        if b == blist[0]:
                            b.fadein()
                        elif blist[blist.index(b) - 1].fade < 80: #start the next fade once the last one reaches a certain percent
                            b.fadein()
                    if b.ishovering(mpos) and blist[-1].faded == True: #if the mouse is hovering over a button, transform it
                        if b.settop(blist):
                            b.transform(1)
                            btop = b
                    else:
                        b.transform(-1) #otherwise, make the transformation go back
                        b.top = False
                    if b.top == False:
                        b.draw()
                if btop is not None:
                    btop.draw()
            if self.fadein < 255:
                self.starting(False)