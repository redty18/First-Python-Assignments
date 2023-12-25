paragraph = input("Enter strings separated by spaces: ").split()
string = ""
print("List of strings:", paragraph)    

for l in paragraph:
    string += (l.capitalize() + " ")
    
print(string)


