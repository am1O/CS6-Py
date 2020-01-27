a = 10000
b = 0.05
f=0
for i in range (1,11):
	a = a + a*b
print("Fees after 10 years will be ${}".format(a))
for i in range (1,5):
	a = a + a*b
	f = f + a
print("Fees for studying 4 years after 10 years will be ${}".format(f))
