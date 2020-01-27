
for i in range(1,7):
    c = i
    for j in range(i,6):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(c,end=" ")
        c-=1
    print("")