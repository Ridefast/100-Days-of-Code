Notes: Multiple If Statements in Succession

Rollercoaster Exercise with the additional Question if a they want to get a Photo. IF Yes 
we will add 3$

Chart: 
https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1
&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEb

Code: 
print("Welcome to the rollercoaster")
bill=0
#Variable "bill" with the value "0"
height=int(input("What is your height "))
if height >=120:
    print("you can ride the Rollecoaster")
    age=int(input("What is your age "))
    if age < 12:
        bill=5
        print("Child Price is $5")
    elif age <= 18:
        bill=7
        print ("Youth Price is $7")
    else:
        print("Adult Price is $12")
        bill=12
    wants_photo=input("Do You want a Photo. Answer wit Y or N ")
    if wants_photo == "Y":
      bill=bill+3
      print(f"Your final bill is {bill}")
    else:
        print(f"Your bill is {bill}")
else:
    print("you can't ride the rollecoaster")

Reminder: 
Line 30: bill=bill+3 is the same as bill+=3
Indetations are very very Important. If that is not right the Code will fail. 





