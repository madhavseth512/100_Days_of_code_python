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

# Mathematical Operators
print(23+43)
print(93-25)
print(3*2)
# Here in python programming language the division gives the result in float data type
print(6/3)
# Exponential mathematical operator is ** (2^3 is written as) -
print(2**3)

# round((What_you_want_to_round_off),precision) function rounds off our numerical value
print(round(6.7))  # This rounds off all the decimal values
print(round(5.6666, 2))  # Rounds off the number to 2 decimal places i.e. result - 5.67

# FLOOR DIVISION
# The floor division discards the decimal part and gives only the integer and on running the type check
# on the output we get int data type
print(10 // 3)  # Output - 3
print(15 // 9)  # Output - 1

# F-Strings
# These are called formatted strings.
# It is to embed all the data types into the strings without converting them into strings.
height = 1.8
isWinning = True
score = 41
# Notice that in the syntax we have used the letter f in front of double/single quotes
# Used curly braces for variable names which are of other data types
print(f"Your score is {score}. Your height is {height}. The prob that you are winning is {isWinning}")

# Unlike C++ if both the numerator and denominator are of integer data type then the answer would be in float data type.
print(5/2)

