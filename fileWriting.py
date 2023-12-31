import csv

newFile = "newFile.txt"

list = [1,2,3,4,5,6,7,8,9]

with open(newFile, "w") as file:
    for num in list:
        writer = file.write(str(num) + '\n')

newCSVFile = "newCSVFile.csv"

listOfLists = [["Adit" , 20] , ["Bob" , 21] , ["Joe" , 45] , ["Anna" , 34]]

with open(newCSVFile, "w", newline='') as csvfile:
    writer2 = csv.writer(csvfile)
    writer2.writerow(['Name', 'Age']) # To write the header, must be outside for loop or itll print too many times
    for lists in listOfLists:
        writer2.writerow(lists) # The writerow function lets you put in list into csv file
