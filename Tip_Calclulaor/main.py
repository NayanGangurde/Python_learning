print("Welcome to the tip calculator")

total_bill=int(input("What was the total bill ?"))
tip=int(input("How much tip would you like to give ? 10, 12 or 15 ? "))
num_of_people=int(input("How many people to split the bill ?"))

share_per_person= round((total_bill+(total_bill * tip/100))/num_of_people,2)

print("Each person should pay " + str(share_per_person))
