# LOOPING STATEMENTS
# For loop : In python this is the syntax of the for loop.

# Here number is a PLACEHOLDER VARIABLE that that will take on the value of
# each element in the sequence during each iteration of the loop. You can choose any valid variable name for this

# Here the list1 can be any iterable object in python such as list, tuple, string or any custom-made object which
# allows iteration

# All the indented block of code below for loop becomes the loop body
list1 = [1, 4, 3, 5, 6, 7, 2]
index = 0
for number in list1:
    print(f"printing the number at index {index} : {number}")
    print(number)
    index = index + 1
print("Line to check how indentation affects the for loop")


# Using the for loops with range() function
# This prints the numbers in the range 1-10
# Notice that the range function does not include the last number 11
for values in range(1, 11):
    print(values)

# By default, the range function increments the value by 1. If we have to increment the value by any other
# value then the syntax would be as follows -
for values in range(1, 11, 2):  # Here the increment would be of 2 instead of 1
    print(2*values)

# Adding up all the numbers in for loop using the range function
sum_numbers = 0
for num in range(1, 101):
    sum_numbers = sum_numbers+num
print(sum_numbers)
