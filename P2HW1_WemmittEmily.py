#Emily Wemmitt
#6/23/2025
#P2WH1
#Calculating travel expenses CONTINUED

print('\t'"-----Calculating Travel Expenses-----")
budget = int(input("Enter Budget:"))
destination = input("Enter your travel destination:")
gas = int(input("Estimate of how much you will spend on gas:"))
lodge = int(input("How much do you think you will spend on lodging:"))
food = int(input("How much will you spend on food:"))

print('\t'"-----Travel Expenses-----")
print(f"{"Location:":20} {destination}")
print(f"{"Initial Budget:":20} ${budget:.2f}")
print(f"{"Fuel:":20} ${gas:.2f}")
print(f"{"Lodging:":20} ${lodge:.2f}")
print(f"{"Food:":20} ${food:.2f}")
print('\t'"-------------------------")
print("Remaining Balance:", budget - (gas + lodge + food))
        
