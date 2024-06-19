# RANDOMISATION IN  PYTHON
# The random module of python is a built-in library that allows us to generate random numbers and perform
# various randomisation tasks. It is to be noted that these are pseudo random numbers which means they are
# deterministic and reproducible based on a seed value


# Importing random module. A module in brief is a python file that containing python definitions and statements
import random
# This functionality is used for printing a random integer between 10 and 20 both included
random_integer = random.randint(10, 20)
print(random_integer)

# Printing a random floating point number between 0 and 1. 1 is excluded
random_float = random.random()
print(random_float)

# To print a random floating point number between 0 and 5 we can do
number = random_float * 5

# To randomly print heads and tails when the program runs
coin_side = random.randint(0, 1)
if coin_side == 1:
    print("Heads")
else:
    print("Tails")

# PYTHON LISTS
# These are ordered, mutable and allows us to store collection of data under a single variable name
# Arrays in C++ can store only values of particular data types.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [10.5, True, "hello"]
nested_list = [[1, 2, 3], ["a", "b", "c"]]

# We can access the elements of the index using both positive and negative index. Starting index is 1 and negative
# index like -1 is the index of last element of the list. negative counting starts from back
print(mixed_list[-1])  # This will print - hello

# Append function adds the single element to the end of the list.
fruits.append(5)
print(fruits)

# Extend function is used to add multiple items to the list
fruits.extend(["mango", "watermelon", "pineapple"])
print(fruits)

# We can use the len() function to calculate the length of the string as well as the list
print(len(numbers))

# IndexError - When we try to access that index of the list which exceeds its max index then this error occurs

# This would print out the list of lists
# NESTED LISTS
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["love", "hello", "bye", "girl"]
combined = [list1, list2]
print(combined)
# Accessing the element from a nested list is done in the same way as we do in C++
print(combined[0][3])  # This will print 3 as output.

