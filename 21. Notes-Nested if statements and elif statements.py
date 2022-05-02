Notes: Nested if/else statements and elif statements

Flow Chart: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload

Nested if/else condition

Example:        if condition:
                    if another condition:
                        do this
                    else:
                        do this
                else: do this

Code Example:   print("Welcome to the rollercoaster")
                height=int(input("What is your height"))
                if height >=120:
                    print("you can ride")
                    age=int(input("What is your age"))
                    if age <= 18:
                        print("Please pay $7")
                    else:
                        print("Please pay $12")
                else:
                    print("you can't ride the rollecoaster")

If/Elif/else condition:

Flow Chart: https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload

Example:        

if condition1:
    do a
elif condition2:
    do b
else :
    do this

Code Example:   
print("Welcome to the rollercoaster")
height=int(input("What is your height"))
if height >=120:
    print("you can ride")
    age=int(input("What is your age"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print ("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("you can't ride the rollecoaster") 

Remember: we can use ass much elifs as we want. 

