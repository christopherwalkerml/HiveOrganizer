#this function returns the time string to blit onto the screen, and the position (that will center the text on the screen)
from pages.scripts.timeformat import *
from pages.scripts.centertext import *
import time

def updatecenter(curtime, winwid, winhig, font):
    formattedtime = timeformat(curtime[0]) #format the time to "XX:XXam/pm"
    if len(str(curtime[1])) == 1:
        curtime[1] = str('0' + str(curtime[1]))
    if int(time.time()) % 2 == 0:
        timedisplay = str(formattedtime[-5::-1][::-1]) + str(curtime[1]) #make the formatted time a proper text display
    else:
        timedisplay = str(formattedtime[-6::-1][::-1]) + ' ' + str(curtime[1])
    centertime = centertext(timedisplay, font, winwid, winhig)
    centerampm = centertext(formattedtime[-2::], font, winwid, winhig + 60)
    return timedisplay, formattedtime, centertime, centerampm