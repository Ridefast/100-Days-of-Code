Exercise: Variacles

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#python code to write 
a,b = b,a

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

Solution:   Line 11
Reason:     Without a temporary variable (Tuple swap)
            Another way to swap the values of two variables, without using a temporary variable, 
            is to use tuple packing and sequence unpacking. Tuples can be constructed in a number of ways, 
            one of which is by separating tuple items using commas. Moreover, Python evaluates the right-hand
            side of an assignment before its left-hand side. So, by separating the variables with commas on the
            right side of the statement the variables are packed into a tuple and unpacked by placing the same
            number of comma-separated target variables on the left side.

            This method of variable swapping and permutation can be used for more than two variables as long as the same
            number of variables are on both sides of the statement.

Source:     https://www.30secondsofcode.org/articles/s/python-swap-variables
