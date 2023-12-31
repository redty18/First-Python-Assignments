list = [1,2,3,4,5,7,9]
list2 = [3,5,7,9,11,1,23,25]

commonInList = []

for num in list:
    for nums in list2:
        if num == nums:
            commonInList.append(num)

print(commonInList)