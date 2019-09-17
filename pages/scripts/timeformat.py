#turn 24 hour clock format into 12 hour format with am/pm
def timeformat(h_24):
    h = h_24 % 12;
    if h == 0:
        h = 12;
    if h_24 < 12:
        ampm = 'am'
    else:
        ampm = 'pm';
    if h < 10:
        return str(h) + ':00' + ampm;
    else:
        return str(h) + ':00' + ampm;
