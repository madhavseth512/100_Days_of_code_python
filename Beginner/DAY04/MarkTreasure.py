# Here we have to take the input as A1, B3, C2 etc as the position in the nested lists and replace it with the
# X symbol which denoted out treasure

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
row = int(position[1])-1
column = position[0].upper()

if column == 'A':
    column = 0
elif column == 'B':
    column = 1
else:
    column = 2

# Instead of this we can alternatively write the code as -
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# This index() function returns the index of the letter variable found in the abc list.
# column_index = abc.index(letter)


map[row][column] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


