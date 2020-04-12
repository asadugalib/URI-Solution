#1134
Alcohol = 0
Gasoline = 0
Diesel = 0

while True:
    
    user_input = int(input())
    
    if user_input == 1:
        Alcohol += 1
    elif user_input == 2:
        Gasoline += 1
    elif user_input == 3:
        Diesel += 1
    elif user_input == 4:
        break

print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(Alcohol, Gasoline, Diesel))
