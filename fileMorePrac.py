import csv

totalSalary = 0
totalEmployees = 0
maxSalary = 0
maxSalaryEmployee = ""
departmentCounts = {}

with open('employees.txt', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        name, department, salary, years_of_experience = row
        salary = int(salary)
        totalSalary += salary
        totalEmployees += 1

        if salary > maxSalary:
            maxSalary = salary
            maxSalaryEmployee = name

        if department in departmentCounts:
            departmentCounts[department] += 1
        else:
            departmentCounts[department] = 1

if totalEmployees > 0:
    averageSalary = totalSalary / totalEmployees
else:
    averageSalary = 0

print(f"Average Salary: {averageSalary}")
print(f"Employee with the Highest Salary: {maxSalaryEmployee} ${maxSalary}")
print("Number of Employees in Each Department:")
for department, count in departmentCounts.items():
    print(f"{department}: {count}")