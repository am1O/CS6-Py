a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))

if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
    p = a + b + c
    print("Valid input\n")
    print("Perimeter = " + str(p))
else: 
    print("Invalid input")