a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
d = int(input("Enter value of d:"))
e = int(input("Enter value of e:"))
f = int(input("Enter value of f:"))

if((a*d - b*c) == 0):
    print("No solution exists")
else:
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print("Solution: x= " + str(x) + " y= " + str(y))