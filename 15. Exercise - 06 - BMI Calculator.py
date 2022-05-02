height = input("enter your height in m: ")
#Output ist type string
weight = input("enter your weight in kg: ")
#Output ist type string
height=float(height)
#Type Change from string to float
weight=float(weight)
#Type Change from string to float
print(round(weight/height ** 2))
#print 75/168x2=26.57 = rounded = 27


#Angelas Solution

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)