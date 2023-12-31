runTime = True

while runTime:
    temp = int(input("Enter a temperature in either Celsius or Fahrenheit: "))
    convert = input("Would you like to convert to Fahrenheit or Celsius (F or C): ")
    if convert == "F":
        newTempF = (temp * 1.8) + 32
        print("Your temperature in Fahrenheit is: " + str(newTempF))
    if convert == "C":
        newTempC = (temp - 32) * (5/9)
        print("Your temperature in Celsius is: " + str(newTempC))
    cont = str(input("Would you like to continue (Y or N): "))
    if cont == "Y" or cont == "y":
        runTime = True
    else:
        runTime = False
    