#1094

test = int(input())

case = []
total_case = 0
rabbit = 0
rat = 0
frog = 0

for i in range(test):
    
     case.append(input().split())

for i in case:
    
    total_case += int(i[0])
    if i[1] == "C":
        rabbit += int(i[0])
    elif i[1] == "R":
        rat += int(i[0])
    elif i[1] == "S":
        frog += int(i[0])
        
per_rabbit = (rabbit / total_case) * 100
per_rat = (rat / total_case) * 100
per_frog = (frog / total_case) * 100

print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}".format(total_case,rabbit,rat,frog))
print("Percentual de coelhos: {:0.2f} %\nPercentual de ratos: {:0.2f} %\nPercentual de sapos: {:0.2f} %".format(per_rabbit,per_rat,per_frog))

#alternate 1094

n=int(input())
C=0
R=0
S=0

for i in range(n):
    
    a,ch=list(map(str,input().split()))
    a=int(a)
    if(ch == 'C'):
        C += a
    elif (ch == 'R'):
        R += a
    else:
        S += a
        
total=C+R+S

x=(C*100.00)/total
y=(R*100.00)/total
z=(S*100.00)/total

print("Total: {} cobaias".format(total))
print("Total de coelhos:",C)
print("Total de ratos:",R)
print("Total de sapos:",S)
print("Percentual de coelhos: %.2lf %%"%x)
print("Percentual de ratos: %.2lf %%"%y)
print("Percentual de sapos: %.2lf %%"%z)
