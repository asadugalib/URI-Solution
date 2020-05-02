#1848 Counting Crow

sm = 0
count = 0

while True:
    crow = input()
    if crow == "caw caw":
        count += 1
        print(sm)
        sm = 0
        if count == 3:
            break
    binary = ""
    for i in crow:
        if i == "*":
            binary += "1"
        else:
            binary += "0"
    sm += int(binary, 2)
