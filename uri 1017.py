#1017
mileage = 12
hour = int(input())
avg_speed = int(input())

distance = hour*avg_speed
fuel = distance/mileage

print("%0.3f"%fuel)
