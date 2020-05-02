#1828 Bazinga!

def game(p1, p2):
    if p1 == p2:
        return "De novo!"
    elif ((p1 == "pedra" and p2 == "tesoura") or (p1 == "papel" and p2 == "pedra") or (
            p1 == "tesoura" and p2 == "papel") or (p1 == "pedra" and p2 == "lagarto") or (
            p1 == "lagarto" and p2 == "Spock") or (p1 == "Spock" and p2 == "tesoura") or (
            p1 == "tesoura" and p2 == "lagarto") or (p1 == "lagarto" and p2 == "papel") or (
            p1 == "papel" and p2 == "Spock") or (p1 == "Spock" and p2 == "pedra")):
        return "Bazinga!"
    else:
        return "Raj trapaceou!"


test = int(input())
count = 1

while count <= test:
    sheldron, raj = input().split()
    result = game(sheldron, raj)
    print("Caso #{}: {}".format(count, result))
    count += 1
