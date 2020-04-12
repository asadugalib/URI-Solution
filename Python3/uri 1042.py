#1042
list1 = list(map(int, input().split()))

temp = list1.copy()
list1.sort()

for i in range(len(list1)):
    print(list1[i])

print()

for i in range(len(temp)):
    print (temp[i])
