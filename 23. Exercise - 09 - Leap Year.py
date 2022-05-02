#Links 
#https://www.youtube.com/watch?v=xX96xng7sAE
#https://replit.com/@appbrewery/day-3-3-exercise?v=1

year = int(input("Which year do you want to check? "))
if year % 4 > 0:
    print ("Not Leap Year")
elif year % 400 == 0:
    print ("Leap Year")
elif year % 100 == 0:
    print ("Not Leap Year")
else:
    print ("Leap Year")
    
#Angelas Solution

#year = int(input("Which year do you want to check? "))
#Refer to the flow chart here: https://bit.ly/36BjS2D
#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#     print("Not leap year.")