#1013
data = input().split(" ")
a,b,c = int(data[0]), int(data[1]), int(data[2])

major_ab = (a+b+abs(a-b))/2
major = (major_ab+c+abs(major_ab-c))/2

print("{:0.0f} eh o maior".format(major))
