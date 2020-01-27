def getDivisors(n) : 
    list = []
    i = 1
    while i < n : 
        if (n % i==0) : 
            list.append(i) 
        i = i + 1
    return list
print("Perfet Numbers: ")
for i in  range (2,10000):
	divs = getDivisors(i)
	if(sum(divs) == i):
		print(i)
