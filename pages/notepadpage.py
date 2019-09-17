#this page controls the notepad page

from pages.pageparent import *
from pages.objects.notepadobject import *
from pages.objects.backbutton import *

class notepadpage(pageparent):

    def __init__(self):
        pageparent.__init__(self)
        self.notepadlist = []

    def startup(self):
        notepads = []
        if os.stat(dir + r'\notepad\sdata.txt').st_size != 0:  # check to see if the file isn't empty
            file = open(dir + r'\notepad\sdata.txt', 'r')  # load data from file and make files
            for lines in file:
                notepads.append(eval(lines.strip()))
            file.close()

        findex = open('datapass.txt', 'r')  # file index
        index = findex.readline().strip()
        if index is not None and len(notepads) > int(index):  # import the index of the button that was pressed so it can load the proper file
            importfile = notepads[int(index)]
        else:
            importfile = None

        if importfile is not None:
            for i in range(len(importfile)):
                self.notepadlist.append(notepadobject(self.win, importfile[i][0], importfile[i][1], importfile[i][2], importfile[i][3]))

        self.buttonlist.append(backbutton(self.win, 'notepadmenupage'))

        self.buttonlist.append(notepadobject(self.win, (100, 100), 'file test', ['zippo', 'potato', 'stone'], False))

    def draw(self, mpos):
        if self.fadeout < 225:
            self.finishing()
        else:
            self.win.fill(HIVE) #draw the background, and decorate it, then draw all the files
            self.decorate()
            delobj = None
            for b in range(len(self.buttonlist)):
                self.buttonlist[b].draw(mpos)
                if self.buttonlist[b].canhover:
                    if self.buttonlist[b].delete:
                        delobj = b
            if delobj is not None:
                del self.buttonlist[delobj]
            if self.fadein < 255:
                self.starting(True)

    def run(self):
        pass