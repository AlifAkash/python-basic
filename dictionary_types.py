monday_temperature = [8.7, 7.9, 10.0, 8.7, 9.6, 5.4]
student_grades = {"marry" : 8.7,"sam" : 7.9,"john": 10.0,"andrew": 8.7,"mike": 9.6,"van": 5.4}

mysum = sum(student_grades.values())
lenght = len(monday_temperature)

mean = mysum / lenght

#myConunt = student_grades.values().count(8.7)

print(mysum)
print(lenght)
print(mean)