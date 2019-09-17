#gets the current time, and outputs [hour, minute]
import time
def gettime():
    localtime = time.localtime(time.time())
    curtime = [localtime[3], localtime[4]]
    return curtime
