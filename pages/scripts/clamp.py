#this function is given a number, and a maximum and minimum value. then returns the number within the range

def clamp(num, maxnum, minnum):
    if num < minnum:
        return minnum
    elif num > maxnum:
        return maxnum
    else:
        return num