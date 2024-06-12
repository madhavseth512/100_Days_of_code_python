# Data Types
# Strings
# Here using the square brackets we can access the elements of the strings
variable = "Hello"[4]
print(variable)
# String concatenation
print("123" + "456")


# Integers
print(123+456)
# for the case of large numbers for better visualization we can use underscores in python language
# Python removes these underscores when it compiles our code
number = 123_453_243_233

# Floating Point Numbers
Float = 0.1245
decimal = 754_45.235

# Boolean Data Type
Bool1 = True
Bool2 = False

# In Python language we can only concatenate string with other string that's why this below code will give error
# num_char = len(input("Enter your name"))
# print("Your name has" + num+char + "characters")
# Here we are concatenating string with integer data type which will give error

num_char = len("Enter your name")
new_num_char = str(num_char)
print("Your name has " + new_num_char + "characters")

# Here using type casting we have converted the data types from one to another
a = float(1235)
b = str(561)

# Here the type function checks the data type of the variable
print(type(a))
print(type(b))

# Here converting the string "100.5" into float. Output will be 170.5
print(70+float("100.5"))
# Here converting the integer data type to string. Output will be 70100
print(str(70)+str(100))


