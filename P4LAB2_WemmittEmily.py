#Emily Wemmitt
#7/3/25
#P4LAB2
#Write a program that asks the user to enter an integer

run_again = "yes"

while run_again == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("This program does not handle negative numbers")
    else:
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    run_again = input("Would you like to run the program again? ")

print("Exiting program...")
