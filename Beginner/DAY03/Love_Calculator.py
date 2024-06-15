# Here we are going to calculate a love score between two people
# Steps are - Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2-digit number.
# Also give the appropriate message based on their love score

print("The love calculator is calculating your score\n")
name1 = input("Enter first name\n")
name2 = input("Enter second name\n")

combine_name = name1+name2

# We convert all the uppercase letters in the combine_name string to lowercase
lowercase_name = combine_name.lower()

t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")
e = lowercase_name.count("e")
digit1 = t+r+u+e

l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")
digit2 = l+o+v+e

# Here we can print specific messages based on the range of score using if-elif-else statements
print(f"Your love score is {digit1}{digit2}")


