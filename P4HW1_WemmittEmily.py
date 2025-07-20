#Emily Wemmitt
#7/6/25
#P2HW2
#Design a program to show grades


#------------------------------
#Puesdo code:
#Enter how many grades you'd like to input
#Put all grades in a list named "module_grades"
#Calculate the lowest grade, modified list, average and letter grade
#Display results
#------------------------------


num_scores = int(input("How many scores would you like to enter? "))

module_grades = []

while len(module_grades) < num_scores:
    score = float(input(f"Enter Grade #{len(module_grades) + 1}: "))
    if 0 <= score <= 100:
        module_grades.append(score)
    else:
        print("INVALID Score entered!!!! Score should be between 0 and 100")

original_grades = []
for grade in module_grades:
    original_grades.append(grade)

lowest = min(module_grades)
module_grades.remove(lowest)

average = sum(module_grades) / len(module_grades)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("----------Results----------")
print(f"{"Lowest Grade:":20} {lowest}")
print(f"{"Modified List:":20} {module_grades}")
print(f"{"Scores Average:":20} {average:.2f}")
print(f"{"Letter Grade:":20} {grade}")
print("---------------------------")
