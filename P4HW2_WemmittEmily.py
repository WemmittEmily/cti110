#Emily Wemmitt
#7/7/25
#P4HW2
#Create a program that shows salary

#Ask users to enter name of employee
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

standard_hours = 40
overtime_rate = 1.5

employee_name = input("Enter employee's name or 'Done' to terminate:" )

while employee_name != "Done":
    hours_worked = float(input("Enter number of hours worked: " ))
    pay_rate = float(input("Enter pay rate: "))

    if hours_worked > standard_hours:
        overtime_hours = hours_worked - standard_hours
        regular_hours = standard_hours
    else:
        overtime_hours = 0
        regular_hours = hours_worked
    employee_name = input("Enter employee's name or 'Done' to terminate:" )    
#calculations

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * overtime_rate
gross_pay = regular_pay + overtime_pay

total_regular_pay += regular_pay
total_overtime_pay += overtime_pay
total_gross_pay += gross_pay
employee_count += 1 

#results

print(f"\nEmployee name: {employee_name}")
print("Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<14.2f}")


print(f"Total employees entered: {employee_count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
