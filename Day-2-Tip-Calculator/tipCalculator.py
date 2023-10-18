#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? \n$"))

tip = input("What percentage tip would you like to give? 10, 12, or 15? \n")

tip_percentage = float("1." + tip)

number_of_people = int(input("How many people to split the bill? \n"))

bill_calculator = (total_bill / number_of_people) * tip_percentage

each_should_pay = round(bill_calculator, 2)
each_should_pay = "{:.2f}".format(bill_calculator)

print(f"Each person should pay: ${each_should_pay}")
