import csv

with open("data.csv", "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data = list(csv_reader)
    filteredRows = []
    for row in data:
        if int(row["Age"]) >= 30 and int(row["Salary"]) <= 50000:
            filteredRows.append(row)
    print(filteredRows)
    
with open("filtered_data.csv" , "w", newline='') as csvfile:
    fieldnames = ["Name", "Age", "Salary"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(filteredRows)

