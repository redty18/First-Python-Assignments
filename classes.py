# Without classes
car1_make = "Toyota"
car1_model = "Camry"
car1_year = 2020

car2_make = "Honda"
car2_model = "Accord"
car2_year = 2021


# With classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating instances of the Car class
car1 = Car(make="Toyota", model="Camry", year=2020)
car2 = Car(make="Honda", model="Accord", year=2021)

# Accessing properties becomes more organized
# print(car1.make)  # Output: Toyota
# print(car2.year)  # Output: 2021
print(car1.make)
print(car1.model)
print(car1.year)
print(car2.make)
print(car2.model)
print(car2.year)

class Dog:
    def __init__(self, name):
        self.name = name

Dog1 = Dog(name="Bob")
print(Dog1.name)

# List representation without classes
# book1 = ["Introduction to Python", "John Smith", 2022, "Programming"]
# book2 = ["Data Science Handbook", "Alice Johnson", 2021, "Data Science"]
# book3 = ["History of Art", "Bob Miller", 2019, "Art"]

class Book:
    def __init__(self, name, author, yearOfPublication, topic):
        self.name = name
        self.author = author
        self.yearOfPublication = yearOfPublication
        self.topic = topic
    def __str__(self):
        return f"MyClass: {self.name}, {self.author} years old, {self.yearOfPublication},{self.topic}"
    def nextPage(self):
        print("Going to next page")

book1 = Book(name="Introduction to Python", author="John Smith", yearOfPublication=2022, topic="Programming")
book2 = Book(name="Data Science Handbook", author="Alice Johnson", yearOfPublication=2021, topic="Data Science")
book3 = Book(name="History of Art", author="Bob Miller", yearOfPublication=2019, topic="Art")

print(book1)
print(book2.author)
print(book3.yearOfPublication)
book1.nextPage()