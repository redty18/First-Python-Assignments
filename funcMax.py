list = [int(x) for x in input("Enter integers separated by spaces: ").split()]

def listMax(list):
    count = 0
    for nums in list:
        if nums > count:
            count = nums
    
    return count


print(listMax(list))
    