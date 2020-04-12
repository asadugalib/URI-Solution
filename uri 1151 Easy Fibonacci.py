#1151 Easy Fibonacci

number = int(input())

term1 = 0
term2 = 1
line = ""

for i in range(number):
    
    line += str(term1)+" "
    next_term = term1 + term2
    term1 = term2
    term2 = next_term

print(line[:-1])
