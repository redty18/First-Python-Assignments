import csv
# reader = csv.reader(csvfile)
# header = next(reader)
    
def sizeOflist(list):
      return len(list)

def sumOfList(list2):
    count1 = 0
    for num in list2:
        count1 += num
    return count1
    
def average(sumOfList, sizeOflist):
     return sumOfList / sizeOflist
bigList = [['Name', 'Average']] 

with open("students.csv", "r") as csvfile:
    print(csv.reader(csvfile))
    listOfLists = []
    count = 0
    reader = csv.reader(csvfile)
    header = next(reader)
    for string in csv.reader(csvfile):
        # if count > 0:
            listOfLists.append(string)
        # count += 1
    # print(listOfLists)
            
    for loopThrough in listOfLists:
          names = loopThrough[0]
          sum = 0
          scores = []
          for num in loopThrough:
                if sum > 0:
                    scores.append(int(num))
                sum += 1
        #   print(names + " " + str(average(sumOfList(scores), sizeOflist(scores))))
          newList = [names, average(sumOfList(scores), sizeOflist(scores))]
          bigList.append(newList)

with open('average_scores.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(bigList)


# def newFunction(readIt):
#     for strings in readIt:
#         name, scores = strings
#         sum = 0
#         for num in scores:
#             sum += num

#         return (sum / len(scores))


# with open("average_scores.csv" , "w") as csvfile:
#     data = [{'Name: ', 'Average: ' + newFunction("students.csv")}]