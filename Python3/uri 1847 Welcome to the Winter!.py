#1847 Welcome to the Winter!

def smile():
    print(":)")


def sad():
    print(":(")


a,b,c = list(map(int, input().split()))

if (-100 <= a <=100) and (-100 <= b <=100) and (-100 <= c <=100):
    if a > b and b <= c:
        smile()
    elif a < b and b >= c:
        sad()
    elif a < b and b < c and (b-a) > (c-b):
        sad()
    elif a < b and b < c and (b-a) <= (c-b):
        smile()
    elif a > b and b > c and (a-b) > (b-c):
        smile()
    elif a > b and b > c and (a-b) <= (b-c):
        sad()
    elif a == b and b < c:
        smile()
    elif a == b and b >= c:
        sad()
