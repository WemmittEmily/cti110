#Emily Wemmitt
#7/12/2025
#P5LAB
#Program self-checkout machine

import random


def disperse_change(change):
    cents = int(round(change * 100))

    if cents == 0:
        print("No change")

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(f"{dollars} dollars")

    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(f"{quarters} quarters")

    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(f"{dimes} dimes")

    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(f"{nickels} nickels")

    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(f"{pennies} pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100), 2)
    print(f"You owe ${amount_owed}")

    cash = float(input("How much cash will you put in the self-checkout? $"))

    change = round(cash - amount_owed, 2)
    disperse_change(change)

main()       
