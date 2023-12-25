password = str(input("Enter a password: "))
loopVar = "lol"
count = 0

for tries in loopVar:
    confirm = str(input("\nConfirm your password: "))
    if confirm != password:
        print("Incorrect confirmation. Try again")
        count += 1
    if confirm == password:
        print("Password confirmed.")
        break

if count > 2:
    print("\nPassword not confirmed after 3 attempts.")


