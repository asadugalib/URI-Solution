#1019
def time_converter(time):
    sec = time % 60
    minute = time//60
    hour = minute//60
    if hour>0:
        minute = minute%60
    return "{}:{}:{}".format(hour,minute,sec)


sec = int(input())

print(time_converter(sec))
