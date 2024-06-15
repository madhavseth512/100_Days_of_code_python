# if-else conditional statement
print("Welcome to the rollercoaster ride")
height = int(input("What is your height "))

# The important parts of the syntax here are the indentation. Same indentation refers to same code blocks
# The semicolons are the integral part of the syntax
if height > 80:
    print("You are eligible for the ride")
else:
    print("You are not eligible for the ride")

# OPERATORS
# CONDITIONAL OPERATORS: greater/less than(>,<), greater/less than or equal to(>=,<=), equal to(==), not equal to(!=)

# Here we are taking input of a number and printing weather it is even or odd
number = int(input("Enter the number "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# We also have nested if-else statement. Here the syntax would be the same just indentation for the sub-condition
# would be different.
age = int(input("Enter your age"))
if height >= 150:  # Here the height variable would contain the value entered above
    if age > 18:
        print("You are eligible to ride")
    else:
        print("You cant rode")
else:
    print("Go and increase your height")

# IF-ELIF-ELSE STATEMENT - When there are multiple conditions to cover, we can add as many elif as we want
age = 21
if age < 18:
    print("Not eligible to ride")
elif age == 18:
    print("Just eligible to ride")
else:
    print("Eligible to ride")

# LOGICAL OPERATORS: and, or, not
a = 12
b = 13
c = 0
print(a and c)  # Output 0
print(b or c)  # Output 13
print(not c)  # Output True

# If we have to type out string in multiple lines then we would use triple quotes
print('''Hello how are you.
This would appear in the next line.
Example of the use of triple quotes in a code. 
''')

# Suppose we are taking string input from the user and then comparing that string to another string
# But we are not restricting the user to be case specific. So we can convert in input string into
# lowercase or uppercase and then compare it
str_variable = input("Enter a string to convert the entered string while taking the input into lowercase").lower()
print(str_variable)

