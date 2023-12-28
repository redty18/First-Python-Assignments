           
# list = [[1,2,3,4,5] , [1,2,3,4,5]]

# for n in list:
#     sum = 0
#     for i in n:
#         sum += i
#     print(sum)
# def printlist(list1):
#     print(list1)

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def sumlist(list2):
#     sum1 = 0
#     for num1 in list2:
#         sum1 += num1
#     return sum1


# for list in matrix1:
#     print(sumlist(list))
#     sum = 0
#     # for num in list:
#     #     sum += num
#     # print(sum)


# # print(sumlist([1,2,3,4,5]))


# students = [
#     ('John', (85, 90, 92)),
#     ('Alice', (78, 88, 95)),
#     ('Bob', (92, 89, 86)), 
# ]
# (85, 90, 92)

# def calculate_average(scoreTuple):
#     sum = 0
#     for num in scoreTuple:
#         sum += num
#     return (sum/len(scoreTuple))
    
# print(calculate_average((85, 90, 92)))

# def calculate_final_grades(listOfTuples):
#     finalGradeList = []
#     print(listOfTuples)
#     for tuple1 in listOfTuples:
#         name, scores = tuple1
#         print(name + "'s final grade: " + str(round(calculate_average(scores))))
#         tuple2 = (name, round(calculate_average(scores)))
#         finalGradeList.append(tuple2)

#     return finalGradeList

# paste = calculate_final_grades(students)
# print(paste)
