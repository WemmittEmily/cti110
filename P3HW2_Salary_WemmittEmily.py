#Emily Wemmitt
#6/27/25
#P3HW2
#Create a program that shows salary

#Ask users to enter name of employee
employee_name = input("Enter name of employee:")
hours_worked = float(input("Enter number of hours employee worked this week:"))
pay_rate = float(input("Enter employee pay rate:"))

standard_hours = 40
overtime_rate = 1.5

if hours_worked > standard_hours:
    overtime_hours = hours_worked - standard_hours
    regular_hours = standard_hours
else:
    overtime_hours = 0
    regular_hours = hours_worked
    
#calculations

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * overtime_rate
gross_pay = regular_pay + overtime_rate

#results

print(f"\nEmployee name: {employee_name}")
print("Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<14.2f}")

