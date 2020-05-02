#1176 Fibonacci Array

def fibonacci(pos):
    t1 = 0
    t2 = 1
    fib = 0
    for i in range(pos):
        fib = t2
        t2 = t1+t2
        t1 = fib
    return fib

test = int(input())

for i in range(test):
    pos = int(input())
    x = fibonacci(pos)
    print("Fib(%d) = %d"%(pos,x))
