#Emily Wemmitt
#6/27/25
#P3LAB

amount = float(input("Enter the amount of money as a float:"))

cents = int(amount * 100)

dollars = cents // 100
cents = cents - (dollars * 100)
if dollars == 1:
    print("1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

quarters = cents // 25
cents = cents - (quarters * 25)
if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

dimes = cents // 10
cents = cents - (dimes * 25)
if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

nickels = cents // 5
cents = cents - (nickels * 5)
if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{pennies} pennies")

pennies = cents
if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")

else:
    print("No change")
