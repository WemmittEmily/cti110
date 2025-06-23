#Emily Wemmitt
#6/23/2025
#P2LAB2
# write code that uses a dictionary to store user input and displays output to the user

cars_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}


keys = cars_mpg.keys()

print("Cars:", keys)

car_choice = input("Enter a vehicle to see it's mpg:")

mpg = cars_mpg[car_choice]

print(f"The {car_choice} gets {mpg} mpg.")

miles = float(input("How many miles will you drive the car?"))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f}(s) of gas are needed to drive the {car_choice} {miles} miles.")
      
