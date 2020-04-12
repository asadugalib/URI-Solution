#1040
a,b,c,d = list(map(float,input().split(" ")))

avg = (a*2+b*3+c*4+d*1)/10

print("Media: {:0.1f}".format(avg))

if avg>=7:
    print ("Aluno aprovado.")
elif avg<5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    exam = float(input())
    
    print("Nota do exame: {:0.1f}".format(exam))
    new_avg = (avg + exam)/2
    if new_avg>=5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
        
    print("Media final: {:.1f}".format(new_avg))
