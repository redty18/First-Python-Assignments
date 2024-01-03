# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Not Divisible by 0")
# except BaseException:
#     print("Incorrect Statement")
# else:
#     print("Divisible")
# finally:
#     print("Program Done")

def read_file(filename):
    with open(filename, "r") as file:
        string = file.read()
        print(string)
try:
    read_file("examplee.txt")
except FileNotFoundError:
    print("Incorrect File Name")
except PermissionError:
    print("Not Allowed to Look at File")
