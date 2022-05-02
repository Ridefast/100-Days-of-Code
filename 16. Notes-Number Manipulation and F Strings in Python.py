Notes: Number Manipulation and F Strings in Python

Function:   round(number, digits)
Example:    x=round(5.2452 ,2) = We round the Number "5.2452" to two digits
Reason:     The round() function returns a floating point number that is a rounded version 
            of the specified number, with the specified number of decimals.
            The default number of decimals is 0, meaning that the function will return the
            nearest integer.

Example:    If we check the data type of the above Number we would see that it is data type  "float".
            Let's say we change the data type from "float" to "integer" only one Number would be shown
Code:       print(int(8/3))
Output:     2
Reason:     Data Type integer has no decimal digits. 

Floor Division: 
            Floor Division means that we turn a data type "float" into a data type "integer". 
            Which means, that the Number will be without decimals. 
            
Example:    print(8/3)
            #without Floor Division
Output:     2.6666666666666665 = data Type "float" because "division" always outputs a decimal Nr.
Example:    print(8//3)
            #with floor division
Output:     2 = data type "integer"
Another thing we can do is we can work with the previous Value. 

Example:    result = 8/2
            print(result)
Output:     2.0 - data type "float"

Example:    result = 8/2
            result + = 2
            print(result)
Output:     6.0         

Links: https://www.codingem.com/python-floor-division/

F Strings: 

A formatted string literal or f-string is a string literal that is prefixed
with 'f' or 'F'. These strings may contain replacement fields, which are
expressions delimited by curly braces {}. While other string literals always 
have a constant value, formatted strings are really expressions evaluated at run time.

Source:      https://docs.python.org/3/reference/lexical_analysis.html#f-strings

Example:     score = 0
             print("your score is " + score)
Output:      TypeError: can only concatenate str (not "int") to str
Reason:      We got a String "your score is" but the Variable "score" is a "float".
Solution:    We would be forced to change the Data Type of the "Score" variable value to "String"

With F String this is not neede anymore

Example:      score = 0
              print(f"your score is {score}")
Output:       your score is 0              
Reason:       With "f-string" you can cutdown the manuel Work of inserting/changing data types.
