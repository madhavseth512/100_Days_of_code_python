# Setting the parameters of functions in Python

# Defining the function with parameter a
def number(a):
    print(a)
    a = 4
    # This prints the value of a from inner scope
    print(a)


# Setting up the value of the parameter a
a = 5
# Calling the function
number(a)


# CREATING A FUNCTION TO GREET A PERSON WITH ITS NAME
# This piece of code shows how we can pass the parameters to functions in python
def greet(name):
    print(f"Hey! {name}")
    print(f"How are you today {name}")


name = input("What is your name ? \n")
greet(name)


# FUNCTIONS WITH MULTIPLE PARAMETERS - we add them by sepa rating them with a comma
def marks(call_yourself, no):
    print("\nThis is to test how to pass multiple parameters in the function")
    print(f"{call_yourself} your marks in mathematics is {no}")


call_yourself = "Madhav"
no = 56
marks(call_yourself, no)