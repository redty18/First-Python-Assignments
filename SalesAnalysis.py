import csv

totalSales = []

with open("sales.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = list(reader)
    for row in data:
        totalSales.append(row)

dictionary = {}

for sales in totalSales:
    productName = sales[0]
    price = sales[1]
    quantity = sales[2]

    totalSalesProduct = int(price) * int(quantity)
    dictionary[productName] = dictionary.get(productName, 0) + totalSalesProduct


# with open("total_sales.csv", "w", newline='') as csvfile:
#     fieldnames = ["Product", "Total Sales"]
#     writer = csv.writer(csvfile)
#     writer.writeheader(header)
#     for name in dictionary:
#         print(str(name) + " " + str(dictionary.get(name)))
#         writer.writerows([
#             [name, dictionary.get(name)]
#             ])

with open('total_sales.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product', 'Total Sales'])  # Write the header row
    for product, sales in dictionary.items():
        print(str(product) + str(sales))
        writer.writerow([product, int(sales)])