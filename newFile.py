count = 0

with open("example.txt" , "r") as file:
    content = file.readlines()
    print(len(content))
#     for n in content:
#         count += 1

# print(count)