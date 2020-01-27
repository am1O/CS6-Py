#Printing the loan 

#Entry from user
amount=int(input("Enter the Loan Amount : "))
period=int(input("Enter the Loan Period (in years) : "))
interest=5.0        #interest 
pay=0.0             #Total Amount Which is to be paid
monthly_pay=0.0     #Total monthly amount tobe paid
total_Pay=0.0       #Total Pay 
print("Rate\tMonthly_Pay\tTotal_Pay")       #Output
while(interest<=8):
    pay=(amount*interest*period)/100
    total_pay=pay+amount
    monthly_pay=total_pay/12
    print(interest,"\t",round(monthly_pay,3),"\t",round(total_pay,3))
    interest=interest+(1/8)
    
