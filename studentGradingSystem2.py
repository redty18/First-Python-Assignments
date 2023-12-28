def calculate_average(scoreTuple):
    sum = 0
    for num in scoreTuple:
        sum += num
    return (sum / len(scoreTuple))

students = [
    ('John', (85, 90, 98)),
    ('Alice', (78, 88, 95)),
    ('Bob', (92, 89, 86)),
]

def calculate_final_grades(listOfTuples):
    for tuple1 in listOfTuples:
        name, scores = tuple1
        print(name + "'s final grade: "  + str(round(calculate_average(scores))))

print(calculate_final_grades(students))
        