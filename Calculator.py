print("Simple Calculator")
print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = int(input("Enter your choice (1 - 5): "))
    if choice == 5:
        print("Calculator Exited")
        break
    operand1 = int(input("Enter operand 1: "))
    operand2 = int(input("Enter operand 2: "))
    if choice == 1:
        print("Result: " + str(operand1 + operand2))
    elif choice == 2:
        print("Result: " + str(operand1 - operand2))
    elif choice == 3:
        print("Result: " + str(operand1 * operand2))
    elif choice == 4:
        print("Result: " + str(operand1 // operand2))
        


