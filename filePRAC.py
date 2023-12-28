def write(path2):
    with open(path2 , "w") as file:
        file.write("1 3 5 7 9 11 13 15 17 19 21")

def read(path):
    with open(path , "r") as file:
        string = file.read()
        list = [int(x) for x in string.split()]
        print(list)

write("example.txt")
print(read("example.txt"))