def area(a,b=1):
    return a * b

l = int(input("Enter a length: "))
width = str(input("Do you want to enter a width: "))
if width == "Yes" or width == "yes":
    w = int(input("Enter a width: "))
    print(area(l,w))
else:
    print(area(l))