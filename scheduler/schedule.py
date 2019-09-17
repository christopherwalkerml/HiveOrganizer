#this module makes a to-do list for the user
#it self-adjusts depending on when the user finishes a task
import os, sys
from pages.scripts.gettime import *
schedules = []

dir = os.path.dirname(os.path.realpath(sys.argv[0]))

def timetosecs(atime):
    secs = atime[0] * 31556926 #years
    secs += atime[1] * 2629743.83 #months
    secs += atime[2] * 86400 #days
    secs += atime[3] * 3600 #hours
    secs += atime[4] * 60 #minutes
    secs += atime[5] * 1 #seconds

def timediff(time1, time2):
    diff = timetosecs(time2) - timetosecs(time1)

class task:

    def __init__(self, name, duration, isdone, num, telapsed, worktype, sched):
        self.name = name
        self.duration = duration * 60 #in seconds
        self.num = num
        self.worktype = worktype
        self.telapsed = telapsed * 60 #in seconds
        self.isdone = isdone
        self.percent = (self.telapsed / self.duration) * 100
        self.sched = sched

    def __repr__(self): #print legible stuff instead of random garbage
        return str([
            self.name,
            self.duration / 60, #return in minutes, because importing imports it as minutes and turns it to seconds. also easier to read in minutes
            self.isdone,
            self.num, #is the index in the tasklist
            self.telapsed / 60, #return in minutes, because importing imports it as minutes and turns it to seconds. also easier to read in minutes
            self.worktype])

class schedule:

    def __init__(self, name):
        self.name = name
        self.tasklist = []
        self.curtask = None
        self.curtime = 0
        self.active = False
        self.cursecs = time.time()

    def __repr__(self): #print legible stuff instead of random garbage
        return str([
            self.name,
            self.active,
            self.tasklist])

    def addtask(self, name, duration, isdone, num, telapsed, worktype): #(name of task, what time of day, time to accomplish, accomplished (T/F), percent over time)
        inserted = False
        for t in range(len(self.tasklist)):
            if self.tasklist[t].num == num and inserted == False: #this adds a task to the task list where it needs to go. It checks for the index equal to the number, then inserts it before the other number with the same index
                inserted = True
                self.tasklist.insert(num, task(name, duration, isdone, num, telapsed, worktype, self)) #this adds a task object to the tasklist. The task object contains name, pos, time, done, and supposed completion percent
                for x in range(len(self.tasklist) - (num + 1)):
                    self.tasklist[num + x + 1].num += 1 #fix the other positions in the task list so that they are all consistent
        if inserted == False:
            self.tasklist.append(task(name, duration, isdone, num, telapsed, worktype, self))

    def remtask(self, num):
        del self.tasklist[num]
        for b in range(len(self.tasklist) - num): #delete the task, then fix all the numbers of the tasks that came after it
            self.tasklist[num + b].num -= 1

    def startnexttask(self):
        self.curtime = gettime()
        if self.curtask is not None:
            self.curtask.isdone = True
        self.update()

    def run(self):
        if self.active:
            if self.curtask is not None:
                temptime = time.time()
                if self.cursecs != int(temptime):
                    self.cursecs = int(temptime)
                    self.curtask.telapsed += 1
                    temppercent = self.curtask.percent
                    self.curtask.percent = (self.curtask.telapsed / self.curtask.duration) * 100  # calculate the percent done
                    if self.curtask.percent != temppercent:
                        self.save()

    def update(self):
        for t in self.tasklist:
            if t.isdone == False:
                t.iscur = True
                self.curtask = t #if the current task is finished, start the next one
                break
            else:
                t.iscur = False
        else:
            self.curtask = None

    def eta(self):
        totalsecs = 0
        for t in self.tasklist:
            totalsecs += t.telapsed #this returns the estimated time of finish for the schedule in the format [hour, minute]
        timelist = time.localtime(time.time() + totalsecs)
        return [timelist[3], timelist[4]]

    def save(self):
        if os.stat(dir+'\scheduler\sdata.txt').st_size != 0:
            ishere = False
            file = open(dir+'\scheduler\sdata.txt', 'r')
            lines = []
            for f in file:
                line = eval(f.strip())
                if line[0] == self.name:
                    ishere = True
                    lines.append(repr(self)) #go through all the schedules in the list and check if they are the current one
                else:                           #if the current one exists and is being changed, change it, then put it all back in the file
                    lines.append(eval(f.strip())) #this makes it so we dont need to loop through every object, but only the file.
            if ishere == False:
                lines.append(repr(self))
            file.close()
            file = open(dir+'\scheduler\sdata.txt', 'w')
            for l in lines:
                file.write(str(l) + '\n') #write all the lines into the file
        else:
            file = open(dir+'\scheduler\sdata.txt', 'w') #if the data file is empty, write to it
            file.write(repr(self))