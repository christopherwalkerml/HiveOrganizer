#this is the main program. it controls all the interactions, and sends it to the current page.
#~~~~~~~~~imports~~~~~~~~~#
#modules
import pygame, os

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 26)  # set the position of the window on the monitor

scrninfo = pygame.display.Info()  # this grabs info on the monitor
winwid = scrninfo.current_w
winhig = scrninfo.current_h - 66  # monitor info

dir = os.path.dirname(os.path.realpath(__file__))
hivepng = pygame.image.load(dir + '\images\comb.png')  # import the images for the program

pygame.display.set_icon(hivepng)

win = pygame.display.set_mode((winwid, winhig))
pygame.display.set_caption('Hive')

# win = pygame.display.set_mode((winwid, winhig), pygame.FULLSCREEN) #this can be used for fullscreen later

def setup(file):
    file.win = win
    file.winhig = winhig
    file.winwid = winwid

#####SETUP#####
#~~~~~~~~pages~~~~~~~~#It needs to be imported after the stuff above because the display needs to be set, along with fonts and init()
from pages.menupage import menupage
from pages.menupageparent import menupageparent
from pages.schedulepage import schedulepage
from pages.notepadpage import notepadpage

page = menupage()

setup(page)
page.startup()

clock = pygame.time.Clock()
running = True
clicked = False
pageclicked = None
mpos = (0, 0)

while running:
    keylist = []
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            mpos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                clicked = True
        elif event.type == pygame.MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
        elif event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keylist.append(event.key)

    if pageclicked != 'menupage':
        page.key = keylist

    page.draw(mpos) #let the page draw what it needs to draw
    pygame.display.update()

    if pageclicked != 'menupage':
        page.key = None

    if page.isclicked == True:
        page.isclicked = False
    if clicked:
        clicked = False
        page.isclicked = True
        if page.click(mpos) is not None and page.click(mpos) != True:
            page.isclicked = False
            pageclicked = page.click(mpos)
            if pageclicked == 'menupage': #depending on what button is clicked, it will have a 'destination string' which will come here. The string will determine the next page
                page = menupage()
            elif pageclicked == 'schedulemenupage':
                page = menupageparent('\scheduler\sdata.txt', 'New Schedule', 'schedulepage')
            elif pageclicked == 'notepadmenupage':
                page = menupageparent(r'\notepad\sdata.txt', 'New File', 'notepadpage')
            elif pageclicked == 'todomenupage':
                page = menupageparent(r'\todolist\sdata.txt', 'New List', 'todopage')
            elif pageclicked == 'notepadpage':
                page = notepadpage()
            elif pageclicked == 'schedulepage':
                page = schedulepage()
            elif pageclicked == 'notepadpage':
                page = notepadpage()
            setup(page)
            page.startup()

    clock.tick(60) #60 fps I think lol

pygame.quit()