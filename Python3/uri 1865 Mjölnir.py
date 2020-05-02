#1865 Mjölnir

for i in range(int(input())):
    hero, force = list(map(str, input().split()))
    if hero == "Thor":
        print("Y")
    else:
        print("N")
