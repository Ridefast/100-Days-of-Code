print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?+lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You're at a crossroad. Where do you want to go")
input1=input("Type 'Left' or 'Right'\n").lower()
if input1 == "left":
  print("Brilliant. You made the right choice.\nNow you see an Island.")
  input2=input("Type 'swimm' to Swimm or 'wait' to wait for a boat.\n").lower()
  if input2 == "wait":
    print("Nice Choice again. It's better to wait and get a boat then get eaten by sharks,\nWhen you step on the Island you start to walk around.\nYou find three doors. A yellow, a blue, a red and a one without a color.")
    input3=input("Choose your door. Type Yellow, Blue, Red or any other Color to choose your door\n").lower()
    if input3 == "yellow":
      print("Your a real Master at Work.\nYou found the Treasure and now you get rewareded with Gold.")
    elif input3 == "blue":
      print("That was not the right choice. Behind that door there is no treasure.\nInstead there are wild animals.\nThey where starving for ages and now they eat you alive.\nNo need to say that the GAME is OVER.")
    elif input3 == "red":
      print("That was a hot but wrong Choice.\nAs soon you open the door the burning flames turn you into ashes\nNo need to say that the GAME is OVER for you right?")
  else:
    print("That was the wrong choice.\nOnly a fool would swimm in waters he doesn't know.\nGAME OVER Fool.")
else:
  print("That was the wrong Choice\nYou fell into a Hole and died.\nGAME OVER")