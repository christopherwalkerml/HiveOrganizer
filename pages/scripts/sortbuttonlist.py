def sortbuttonsize(alist):
    blist = alist[:] #this function sorts all the buttons depending on their transformation size so they they blit in order
    size = len(blist)
    newlist = []
    for b in range(size):
        biggest = blist[0]
        for l in blist:
            if l.transforming < biggest.transforming: #if the current button being iterated is larger than the temporary max, change the max
                biggest = l
        newlist.append(biggest) #when the for loop is done, add the next max to the list, and delete it from the iteration list
        blist.remove(biggest)
    return newlist