# printing in python
print("Hello world")
# Can also print this 2 by enclosing it in single quotes
print(2)
print(45+7)
print('A')

# If we have to incorporate the double quotes within our string there are two ways -
# METHOD 1 - By replacing the outer double quotes with single quotes
print('I have added "double quotes" here')
# METHOD 2 - By adding backslash in front of our double quotes
print("I have incorporated the \"double quotes\" here")

# Adding a new line character in python
print("This is my first line\nThis would be my second line")

# String Concatenation - joining multiple strings together to create a new single string
print("Hello"+' '+"Buddy")

# It is very necessary to pay a close look on indentation in Python.
# Python indentation is a way of telling a Python interpreter that the group of statements belongs
# to a particular block of code

# INPUT FUNCTION IN PYTHON
# Here inside the parenthesis there is the prompt that will be displayed before taking the input from user
name = input("What is your name ")
print("Your name is " + name)
# There is a variation to this code
print("Hello " + input("Enter your name again "))

# How to find the number of characters in the string
# The len() function calculates the number of characters here
# We can also put a variable name inside the parenthesis
No_of_letters = len("Madhav")
print(No_of_letters)

# Here we can take input and calculate the length of the string entered and then print the final result by
# this particular piece of code
print(len(input("Enter your name and I will tell you number of characters in it")))

# Instead of this long piece of code I can use variables
Name = input("Enter your name")
length = len(Name)
print(length)







