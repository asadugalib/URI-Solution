#1018
def money(total,note):
    num_notes = total // note
    return num_notes


total = int (input())
notes = [100, 50, 20, 10, 5, 2, 1]
num_notes = []

print (total)

for i in range(len(notes)):
    num_notes.append(money(total,notes[i]))
    total = total % notes[i]
    print ("{} nota(s) de R$ {},00".format(num_notes[i],notes[i]))
