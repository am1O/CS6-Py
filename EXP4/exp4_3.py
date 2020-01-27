list = []
j=0
for i in range(100,1001):
			if(i%30==0):
				list.append(i)
for i in list:
	if(j<9):
		j=j+1
		print("{} ".format(i)),
	else:
		j=0
		print("{} ".format(i))
		
