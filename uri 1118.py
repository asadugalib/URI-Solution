#1118
count = 0
sm = 0
two_score = True
choose = False

while two_score:
    
    score = float(input())
    
    if score > 10 or score < 0:
        print("nota invalida")

    else:
        count += 1
        sm += score

        if count == 2:
            print("media = {:0.2f}".format(sm/2))
            choose = True

            while choose:

                print("novo calculo (1-sim 2-nao)")
                enter = input()

                if enter == "1":
                    count = 0
                    sm = 0
                    choose = False

                elif enter == "2":
                    two_score = False
                    choose = False
