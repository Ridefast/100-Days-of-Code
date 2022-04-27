Notes:  Python Primitive Data Types

String: 
There are many kinds of data types, each different to the computer 
The one we’ve been working with so far has been; strings. Strings
are as simple as their name, think of it like a necklace, every character
you input will be a bead, when you’ve finished your string, your necklace is ready.
If you want to print only a certain character of a string, you can put [] at the end

Example: 
print("Hello Santiago"[1])
Output: 
H

Reason: 
Counting always starts with "0" not with one. So "1" is not the first but the Second Character.
The Method of pulling out particular Elemetns of a String is called "sub-scripting".
The Number between the square Brackets determines which character we are going to pull out.
As long the a Number is in "" it will not be handled as a Number but instead handled as a piece
of Text.

Integer:
Are Numbers without any decimal places. 
Integer Numbers are just wrote down without any sign. 

Example:
Print("123" + "345")
Output: 123456
Reason: The Numbers are in quotations so the are Strings. 

Integer Example:
print(123 + 345)
Output: 468

Reason: No Quotations so it's calculated and the Result of 122+456 is 468

When we write a large Number for example "342,654,896" the comas split the Number so we can read 
it better. Same goes for python. Instead of "," are replaced with underscores. "342_654_896". 
That Number will be read as "342354896". Benefit is to visualize it easier. 

Used in code as int() 
Only whole numbers 
To break it up we don’t use commas, we use underscores since commas will be
considered as something else while underscores will be ignored 
Used to perform mathematical functions e.g addition 
Addition (+) 
Division (/) 
Multiplication (*) 
Exponent (**) 

Float:
Float is the Data Type for Numbers with a Decimal Number like "5.2", Float comes from the Word
"floating Point Number".

Used in code as float() 
These are decimal point numbers. 
Used to perform mathematical functions e.g addition 
Addition (+) 
Division (/) 
Multiplication (*) 
Exponent (**) 
Modulus (%) - this shows the remainder after a division 
Division ALWAYS returns a floating-point number. 

Boolean:
The Data Type Boolean has only two values. "True" or "False". MThey are always written
with a Capital "T or "F".
With the Boolean Data Type we can check if something is True or False.

Written in code as bool() 

Things to Remember: 

Counting always starts with "0"
Integer = int()
float = float()
Boolean = bool()