#the proper way python should round numbers. (good round (ground))
def ground(num):
    if num - int(num) >= 0.5:
        return int(num + (1 - (num - int(num))))
    else:
        return int(num)
