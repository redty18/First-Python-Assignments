def stringReverse(string):
    reverseString = ""
    
    string = str(input("Enter a string: "))
    # Adit reverseString letter
    # adit
    # tida
    for letter in string:
        print(letter)
        reverseString = letter + reverseString
    
    print(reverseString)

stringReverse("string")
