c = '!'
j=0
while(ord(c) != 127):
    if(j<9):
        j=j+1
        print(c),
    else:
        j=0
        print(c)
    c = chr(ord(c) + 1)

   
