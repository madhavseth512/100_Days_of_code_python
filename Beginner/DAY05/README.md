# Day05

## Today we have learnt about: 

- How to write for loop in the python language 
- How to iterate through python lists using for loop
- How to use range function in for loop 
- Indentation plays a very important role in deciding what is inside the for loop and what is outside 
- What is placeholder variable in for loop and how it operates

## Split Function 
The .split() function in Python is a powerful method used to  **split a string into a list of substrings.**  It operates based on a specified delimiter (separator), which is a character or sequence of characters used to mark the division points between desired substrings.
```python
sentence = "This is a string with spaces."

# Splitting at spaces (default behavior)
words = sentence.split()
print(words)  # Output: ['This', 'is', 'a', 'string', 'with', 'spaces.']

# Splitting at commas
words = sentence.split(',')
print(words)  # Output: ['This is a string with spaces.'] (no split occurred)

# Splitting at a specific character or string
words = sentence.split(' ')
print(words)  # Output: ['This', 'is', 'a', 'string', 'with', 'spaces.'] (same as default)

words = sentence.split('is')
print(words)  # Output: ['This ', ' a string with spaces.']

```