set1 = {int(x) for x in input("Enter integers separated by spaces: ").split()}
set2 = {int(x) for x in input("Enter integers separated by spaces: ").split()}

def Subset(set1, set2):
    return set1.issubset(set2)

print(Subset(set1, set2))


