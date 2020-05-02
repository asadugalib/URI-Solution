#1759 Ho Ho Ho

num = int(input())
text = ""
for i in range(num):
    if i == num-1:
        text += "Ho!"
    else:
        text += "Ho "
print(text)
