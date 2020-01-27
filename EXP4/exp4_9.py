amount=int(input("Enter the Loan Amount : "))
years=int(input("Enter the Years : "))
rate=int(input("Enter the Interest Rate : "))
balance=amount
monthlyPayment=amount/12
print("Month\t\tInterest\t\tPrincipal\t\tBalance")
for i in range(1,years*12+1):
    interest=rate*balance
    principal=monthlyPayment-interest
    balance=balance-principal
    print(i,"\t\t",interest,"\t\t",principal,"\t\t",balance)