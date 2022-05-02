#Links:

#https://docs.python.org/3/tutorial/floatingpoint.html
#https://replit.com/@appbrewery/tip-calculator-start
#https://replit.com/@appbrewery/tip-calculator-end
#https://www.adamsmith.haus/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Task:
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#my Code


#Task:
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


#My Code: 
print("Welcome to the tip calculator.")
#print the Welcome Message
bill_total=input("What was the total bill? $")
#Variable with the value of the Userinput
bill_total=float(bill_total)
#data type change from "string" to "float"
tip=float(input("How much would you like to tip: 10, 12, or 15 percent? "))
#new variable "tip" with data type "float" and the value of the userinput
num_people=float(input("How many to split the bill? "))
#new variable "num_people" with the data typ "float" and the value of the Userinput
tip_per_person=(float((bill_total/num_people)*1.12))
#new variable "tip_per_person" wit the data type "float" and with the calculation for 12%
#frage1: wenn man das für mehrere Leute und für alle angegebenen % machen will müsste man die alle
#in neue Variablen reinpacken?
final_tip_per_person="{:.2f}".format(tip_per_person)
#new variable "final_tip_per_person" and the syntax for 2 decimals after the point ""
#see https://www.adamsmith.haus/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print(f"Each person should pay ${final_tip_per_person}")
#print "string" and value of the "final_tip_per_person" variable
#Frage2: Wie würden wir das machen wenn mehr Anzahl leute Container da wären? stichwort: if funktion

#Angelas Code

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
# FAQ: How to round to 2 decimal places?
# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
print(f"Each person should pay: ${final_amount}")