#1015
import math

p1 = input().split(" ")
p2 = input().split(" ")

distance = math.sqrt((float(p2[0])-float(p1[0]))**2+(float(p2[1])-float(p1[1]))**2)

print("%0.4f"%distance)
