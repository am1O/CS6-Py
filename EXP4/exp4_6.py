for i in range(1,7):
    c = 0
    for j in range(i,6):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(2**c,end=" ")
        c+=1
    c = i-2
    for k in range(1,i):
        print(2**c,end=" ")
        c-=1
    print("")
