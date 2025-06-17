#Emily Wemmitt
#6/16/2025
#P1WH2
#Calculating travel expenses

print('\t'"-----Calculating Travel Expenses-----")
budget = int(input("Enter Budget:"))
destination = input("Enter your travel destination:")
gas = int(input("Estimate of how much you will spend on gas:"))
lodge = int(input("How much do you think you will spend on lodging:"))
food = int(input("How much will you spend on food:"))

print('\t'"-----Travel Expenses-----")
print("Location:", destination, '\n'
      "Initial Budget:", budget,'\n'
      "Fuel:", gas,'\n'
      "Lodging:", lodge,'\n'
      "Food:", food)
print("Remaining Balance:", budget - (gas + lodge + food))
        
