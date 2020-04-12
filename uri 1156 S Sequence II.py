#1156 S Sequence II

s = 0

for i in range(1,21):
    
    s += (2*i - 1)/(2**(i-1))

print("%0.2f"%s)
