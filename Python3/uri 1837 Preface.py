#1837 Preface

a, b = list(map(int,input().split()))
q = a//b
r = a % b
if r < 0 or r > abs(b):
    q = q + 1
    r = a-(b*q)
print(q, r)
