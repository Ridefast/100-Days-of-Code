Notes: Python Variables

-   Variables = Imagine you have a Phonebook and you put Numbers in it. Let's say Number
                "12345"" There is no way that we can refer to this Number on a later Point.
                If we give the a Name we can refer to thamt Name. Let's give it the Name
                "hans". So "hans" is the Variable for the Number "12345". 
                
    Example:    name=input("what is your name")
    
    Output:     What is your name - and then the USer has to make a Input. After the Input
                nothing is happening but the Input has been saved in the Variable "name".
                With this we can refer to the input and use it to print the Input.
    
    Example:    name=input("what is your Name")
                print(name)
    
    Output:     What is your name - Then the User makes a Input and that Input is printed
                with the Function print(variable of the input) in our case print(name).

    Example:    print(len(input('What is your name?'))) - Solution of Exercise 03
                #Code without Variables
    
    Example:    name=input("What is your name?")
                lenght=len(name)
                print(lenght)
                #Code with Variables
                
    Output:     What is your name? - The Code is saying that the User Input will be stored 
                in the Variable "name". Then the Variable "lenght" has the function "len()" 
                that will count the lenght of the Name the User has entered. Last thing
                is the "print()" function that prints the result. 