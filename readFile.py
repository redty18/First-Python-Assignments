with open("names.txt", "r") as file:
    names = file.read().split()
    for name in names:
        print(name)