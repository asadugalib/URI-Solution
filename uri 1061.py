#1061

d1 = int(input().split()[1])
h1,m1,s1 = list(map(int,input().split(":")))

d2 = int(input().split()[1])
h2,m2,s2 = list(map(int,input().split(":")))

if s2 >= s1:
    s=s2-s1
else:
    s = 60+s2-s1
    m2 = m2-1
if m2 >= m1:
    m = m2-m1
else:
    m = 60+m2-m1
    h2 = h2-1
if h2 >= h1:
    h = h2-h1
else:
    h = 24+h2-h1
    d2 = d2-1

d = d2-d1

print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(d,h,m,s))
