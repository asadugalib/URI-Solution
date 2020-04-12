#1047
hs,ms,he,me = list (map(int,input().split()))

if hs >= he and ms >= me:
    if ms > me:
        m = 60+me-ms
        h = (24-hs)+he-1
    else:
        m = ms-me
        h = (24-hs)+he
else:
    if ms > me:
        m = 60+me-ms
        h = he-hs-1
    else:
        m = me-ms
        h = he-hs

print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,m))
