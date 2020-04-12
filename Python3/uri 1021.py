#1021
def money(total,note):
    num_notes = int(total / note)
    return num_notes


N = eval(input())
total=float("%0.2f"%N)

if  total>= 0 or total <= 10000000.00:
    notes = [100, 50, 20, 10, 5, 2]
    coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    print ("NOTAS:")
    for i in range(len(notes)):
        num_notes = money(total,notes[i])
        total = total % notes[i]
        total= float("%0.2f"%total)
        print ("{:0.0f} nota(s) de R$ {:0.2f}".format(num_notes,notes[i]))

    print ("MOEDAS:")
    for i in range(len(coins)):
        num_coins = money(total,coins[i])
        total = total % coins[i]
        total= float("%0.2f"%total)
        print ("{:0.0f} moeda(s) de R$ {:0.2f}".format(num_coins,coins[i]))
