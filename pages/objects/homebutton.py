#this button, when clicked, goes to the main page.
#It's this simple because I didn't want the main button to have a destination since a lot of buttons won't require a destination

from pages.objects.mainmenubutton import *

class homebutton(mainmenubutton):

    def __init__(self, win, pos, pic, size):
        mainmenubutton.__init__(self, win, pos, pic, size)
        self.canhover = False
        self.dest = 'menupage'
        self.num = -1

    def update(self):
        pass