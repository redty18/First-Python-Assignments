newData = [1,2,3,4,5]

with open("example.txt", "a") as file: # a = append
    for num in newData:
        file.write("\n" + str(num))