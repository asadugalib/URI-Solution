#1154 Ages

count = 0
ages = 0

while count != "negative":
    
    age = int(input())

    if age >= 0:
        count += 1
        ages += age

    else:
        avg = ages/count
        count = "negative"

print("%0.2f"%avg)
