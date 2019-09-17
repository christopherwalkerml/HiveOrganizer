# this class is the menu button class. It controls the menu buttons
from pages.objects.mainmenubutton import *
import pygame
from pages.colour import *

fontlist = []
for i in range(14):
    fontlist.append(pygame.font.Font(dir+'\pages\Font.ttf', 15 + i)) #make all the sizes of fonts (especially used when buttons grow in size, and the text must adapt)

class menubutton(mainmenubutton):

    def __init__(self, win, pos, pic, size, dest, pic2, size2, text):
        mainmenubutton.__init__(self, win, pos, pic, size)
        self.pic2 = pic2
        self.size2 = size2
        self.transformedsize = self.size
        self.text = text  # text format : [title, sentence 1, sentence 2, ...]
        self.transforming = 0
        self.top = False
        self.fade = 100
        self.faded = False
        self.dest = dest

    def settop(self, buttons): #this function sets the hovered button as the top button to draw
        if not self.top:
            istop = False
            for b in buttons:
                if b.top == True:
                    istop = True
                    break
            if istop == False:
                self.top = True
                return True
            else:
                return False
        else:
            return True

    def fadein(self):
        if self.fade > 0:
            self.fade -= 3 #speed that their alpha increases
            pic1 = self.transformpic(self.pic, self.size, (100 - self.fade / 100), self.transforming) #this changes their alpha upon fade in
            self.win.blit(pic1[0], pic1[1])
            pic2 = self.transformpic(self.pic2, self.size2, (self.fade / 100), self.transforming)
            self.win.blit(pic2[0], pic2[1])
        else:
            self.faded = True

    def transform(self, sign):
        if self.top:
            if sign > 0:
                if self.transforming < 100:
                    self.transforming += 5  #control the transforming with a percent
        else:
            if self.transforming > 0:
                self.transforming -= 5

    def transformtext(self, text, fadepercent, number, cellwid, cellhig):
        if number == 0:
            size = (fadepercent / 0.05)
            addhig = -5
        else:
            size = (fadepercent / 0.1) #this function "fades" the text by changing the colour from hive wall to hive
            addhig = 5
        self.win.blit(fontlist[int(size)].render(text, False, (int(HIVE[0] + ((HIVEWALL[0] - HIVE[0]) * (fadepercent * 1.5))), #this "fades" the text.
                                                               int(HIVE[1] + ((HIVEWALL[1] - HIVE[1]) * (fadepercent * 1.5))), #colour
                                                               int(HIVE[2] + ((HIVEWALL[2] - HIVE[2]) * (fadepercent * 1.5))))),
                                                               ((self.pos[0] - ((cellwid * 0.7) / 2)),
                                                               self.pos[1] - (cellhig / 6) + addhig + ((9 * (fadepercent + 1)) * number))) #position

    def draw(self, mpos = None):
        if self.faded:
            pic1 = self.transformpic(self.pic, self.size, (self.transforming / 150), self.transforming) #transform the first pic and then blit it
            self.win.blit(pic1[0], pic1[1])
            for t in range(len(self.text)):
                self.transformtext(self.text[t], (self.transforming / 150), t, pic1[0].get_width(), pic1[0].get_height()) #draw text on button with alpha
            pic2 = self.transformpic(self.pic2, self.size2, (self.transforming / 100), self.transforming) #transform the second pic then blit it
            self.transformedsize = self.size
            self.win.blit(pic2[0], pic2[1])