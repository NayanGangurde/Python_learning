from traceback import extract_tb

print("Welcome to Python pizza deliveries!")
size=input("What is the size of pizza do you want ? S, M, L:")
pepperoni=input("Do you want pepperoni on your pizza ? Y or N:")
cheese=input("Do you want extra cheese ? Y or N:")

bill=0
if size=="S":
    bill+=15
    if pepperoni=="Y":
        bill+=2
    if cheese=="Y":
        bill+=1
elif size=="M":
    bill+=20
    if pepperoni=="Y":
        bill += 3
    if cheese == "Y":
        bill += 1
else:
    bill+=25
    if pepperoni=="Y":
        bill += 3
    if cheese == "Y":
        bill += 1

print("Your Final bill is "+str(bill))
