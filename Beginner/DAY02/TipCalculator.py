print("Welcome to to tip calculator")
total_bill = int(input("What is the total bill "))
tip = int(input("What is the total tip you would like to give "))
final_bill = total_bill + tip
no_split = int(input("In how many people you have to split the bill "))
each_person = (final_bill / no_split)
print(f"Each person have to pay $ {each_person}")

