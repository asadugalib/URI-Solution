#1048
salary = float(input())

if 0<= salary <=400:
    earned = salary*.15
    new_salary = salary+earned
    per = 15
elif 400< salary <=800:
    earned = salary*.12
    new_salary = salary+earned
    per = 12
elif 800< salary <=1200:
    earned = salary*.1
    new_salary = salary+earned
    per = 10
elif 1200< salary <=2000:
    earned = salary*.07
    new_salary = salary+earned
    per = 7
elif 2000< salary:
    earned = salary*.04
    new_salary = salary+earned
    per = 4

print("Novo salario: {:0.2f}\nReajuste ganho: {:0.2f}\nEm percentual: {} %".format(new_salary,earned,per))
