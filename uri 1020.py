#1020
def day_converter(d):
    year = d//365
    month = (d%365)//30
    day = (d%365)%30
    return "{} ano(s)\n{} mes(es)\n{} dia(s)".format(year,month,day)


day = int(input())

print(day_converter(day))
