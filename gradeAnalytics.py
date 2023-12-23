studentNum = int(input("Enter the number of students in the class: "))
count = 0
math_marks = 0
science_marks = 0
english_marks = 0
a_count = b_count = c_count = d_count = f_count = 0
topPerformer = ""
topPerformerGrade = 0

while count < studentNum:
    name = str(input("\nEnter your name: "))
    grade1 = int(input("Enter your Math Grade: "))
    grade2 = int(input("Enter your Science Grade: "))
    grade3 = int(input("Enter your English Grade: "))
    count += 1
    math_marks += grade1
    science_marks += grade2
    english_marks += grade3
    average_Grade = (grade1 + grade2 + grade3)/3
    if average_Grade > topPerformerGrade:
        topPerformerGrade = average_Grade
        topPerformer = name
    if average_Grade >= 90:
        a_count += 1
    elif average_Grade >= 80:
        b_count += 1
    elif average_Grade >= 70:
        c_count += 1
    elif average_Grade >= 60:
        d_count += 1
    else:
        f_count += 1


if count == studentNum:
    print("\nClass Analytics: ")
    print("Math Average: " + str(math_marks // studentNum))
    print("Science Average: " + str(science_marks // studentNum))
    print("English Average: " + str(english_marks // studentNum))


print("\nGrade Distribution: ")
print("-A: " + str(a_count) + " students")
print("-B: " + str(b_count) + " students")
print("-C: " + str(c_count) + " students")
print("-D: " + str(d_count) + " students")
print("-F: " + str(f_count) + " students")

print("\nTop Performer: " + str(topPerformer) + " (Average Marks: " + str(topPerformerGrade) + ")")



