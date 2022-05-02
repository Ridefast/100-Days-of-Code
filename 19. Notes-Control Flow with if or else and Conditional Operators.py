Notes: Control Flow with if or else and Conditional Operators

Imagine we got a Bathtub and the water lkeeps raising. it will not overflow is because of the overflow.
whenever the water reaches a certain level the overflow will drain the water.

With this example we can explain the "if" or "else" statement. Depending on a particular condition we 
would do either a or b 

Example:        If water level greater then "80cm" = yes = drain the water
                If water level greather then "80cm" = no = continue

Code Example:   if condition:
                    do this
                else:
                    do this
                    
To Remember:    The "if" always is followed by a "do this" that has a tab at the start. This means that 
                that is a block of code. 
                The same counts for the following "else".
                
Example:        if condition:
                    do this = Codeblock of the if function. 
                else
                    do that = Codeblock of the else function
                    
Bath Example:   water_level=90
                if water_level > 80:
                    print("Drain Water")
                else:
                    print("continue")

Output:         Drain Water
Reason:         Water level greather then 80
Remember:       If the "water_level" is exactly "80", "continue" will be printed because we used the ">".
                This means greather then "80". If we want to use "80 or more" we need to use ">=".
                
Another Example is a Rollercoaster where People over 120cm are allowed to ride and people smaler then 120
are not allowed to ride the Rollercoaster.


Example:        height=(int (input("What is your height in cm ")))
                if height >= 120:
                    print("you can ride the Rollercoaster")
                else:
                    print("your are to small to ride the rollercoaster")

Output:         What is your height in cm
                - userinput
                if input 120 or bigger = you can ride the Rollercoaster
                else = your are to small to ride the rollercoaster

Coparison Operators: 

Greather than: >
Less than:     <
Greather then or equal to:  >=
Less than or equal to:      <=

Equal to:       == Checking if the value on the left ist the same as on the right.
Not equal to:   != 

Remenber: One "=" sign means we are assigning a Value to a variable 
          two "==" signs means Checking if the value on the left ist the same as on the right.