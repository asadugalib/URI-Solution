#1174 Array Selection I

array = []

for i in range(100):
    
    array.append(float(input()))
    
    if array[i] <= 10:
        
        print("A[%d] = %0.1f"%(i, array[i]))
