Notes: Type Error, Type Checking and Type Conversion

Data Types and Functions:

Example: 
len(123)

Reason:
Let's say we got a Machine that has to do a Work. Beans --> Coffee Machine --> Coffee.
IF we give it a Rock instead of Beans the Output will not be a Coffee but
we probably brick the Machine.
The "len" Function not likes to work with integars. "123" is a Integar. 
So the Code "len(123)" will turn out a Error. 

Example:
num_char=len(input("what is your name"))
print("your name has" + num_char + "characters")

Here we would think that the Output is the following. 
"What is your Name"
User Input: Hans
"Your Name has 4 characters"

If we print that we will recieve a "TypeError" that tells us that we 
"can only concatenate str (not "int") to str

Reason: 
The class of "num_char" is a "integer" but the rest are strings. 
We can find that out with the "type()" Function. 

Example: 
num_char=len(input("what is your name"))
print(type(num_Chart))

Output: 
what is your name
"User Input" 
<class 'int'>

So any time we are not sure what the Type of date of something might be
we can simply put it inside a Type Check Funtion. 

Type Conversion/Type Casting = Change the Data Type from one particular Data to another

Example: 
num_char - is a "integer" data type and we want to change it to String
str(num_char) - "str" is the data type we want to convert the variable "num_chart" to.
                  Then we save anything into a new Variable called "new_num_chart".
new_num_Char=str(num_char) - Now we can use it in our print statement

#Code with changed data Type. 
num_chart=len(input("what is your name"))
#data type change from integer to string
new_num_chart=str(num_chart)
#print statement with all the same data types
print("Your name has\n" + new_num_chart + " characters.")

Remember: 
We can uske the Type Function to verify the Data we are working with. 
We can use functions like "string", "int" or "float" to convert to that data




       









