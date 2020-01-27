from datetime import datetime
day = int(input("Enter the today's day"))
nos = int(input("Enter the nos day"))

days = [sunday, monday, tuesday, wednesday, thusday, friday, startuday]
fut = (nos//7+ day) if (nos//7+ day) < 7 else (nos//7+ day )//7

print(days[fut])
