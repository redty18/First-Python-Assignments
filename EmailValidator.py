containsAt = False
containsPeriod = False

while True:
    email = str(input("Enter an email: "))
    for l in email:
        if l == "@":
            containsAt = True
        if l == ".":
            containsPeriod = True
    if containsAt == False or containsPeriod == False:
        print("Invalid")
    else:
        print("Valid")
        break

    
        
    

