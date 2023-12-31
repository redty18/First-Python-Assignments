import csv

inputFile = "itemPrice.csv"

totalSales = []

with open(inputFile, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = list(reader)
    for num in data:
        totalSales.append(num)

dictionary = {}

for sales in totalSales:
    prodName = sales[0]
    price = sales[1]
    dictionary[prodName] = dictionary.get(prodName, 0) + int(price)
print(dictionary)