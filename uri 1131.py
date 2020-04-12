#1131
num_game = 0
inter = 0
gremio = 0
draw = 0
new_game = True

while new_game:
    
    num_game += 1
    x, y = list(map(int, input().split()))

    if x > y:
        inter += 1
    elif x < y:
        gremio += 1
    else:
        draw += 1

    while True:

        print("Novo grenal (1-sim 2-nao)")
        d = input()

        if d == "1":
            break
        elif d == "2":
            new_game = False
            break

print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(num_game, inter, gremio, draw))

if inter > gremio:
    print("Inter venceu mais")

elif inter < gremio:
    print("Gremio venceu mais")

else:
    print("Não houve vencedor")
