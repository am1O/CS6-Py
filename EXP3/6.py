mon = int(input("enther the integer for month"))
year = int(input("enther the integer for year"))

from calendar import monthrange
print(monthrange(year, mon))
