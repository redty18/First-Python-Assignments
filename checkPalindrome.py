def checkPalindrome(number):
    string2 = ""

    for letter in str(number):
        string2 = letter + string2

    if str(number) == string2:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


checkPalindrome(123454321)