#1
student_scores = (85, 92, 78, 90, 88)

#2
score = 0
for l in student_scores:
    score += l
print(score/5)

#3
list = []

for n in student_scores:
    if n >= 80:
        list.append(n)

passed_students = tuple(list)
print(passed_students)

#4
count = 0

for i in passed_students:
    if i >= 90:
        count +=1

print(count)

#5
list2 = []

for q in student_scores:
    list2.append(q + 5)

updated_scores = tuple(list2)
print(updated_scores)

#6
print(student_scores)
print(passed_students)
print(updated_scores)