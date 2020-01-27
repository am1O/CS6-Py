nos = int(input("enter the integer here"))
 
if not nos%6 and not nos%5:
  print("both")
elif not nos%6 and nos%5:
  print("6")
elif not nos%5 and nos%6:
  print("5")
  
