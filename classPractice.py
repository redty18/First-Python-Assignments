class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return "Woof Woof"

Dog1 = Dog(name="Bob", breed="Golden Retreiver")
print(Dog1.bark())

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
Rectangle1 = Rectangle(length=10, width=4)
print(Rectangle1.calculate_area())

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, depo):
        self.balance = self.balance + depo
        return self.balance
    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        return self.balance

BankAcc1 = BankAccount(account_holder="Adit", balance=2000)
print(BankAcc1.deposit(10000))
print(BankAcc1.withdraw(1000))
print(BankAcc1.balance)

class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 // num2

calc = Calculator()
print(calc.addition(5,6))
print(calc.subtraction(6,5))
print(calc.multiplication(5,6))
print(calc.division(15,3))

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_circumference(self):
        return 2 * 3.1415 * self.radius

circle1 = Circle(radius=5)
print(circle1.calculate_circumference())

class TemperatureConverter:
    def convertToCelsius(self, origTemp):
        print((origTemp - 32) * 5/9)
    def convertToFahrenheit(self, origTemp):
        print((origTemp * 9/5) + 32)

temp1 = TemperatureConverter()
temp1.convertToCelsius(98)
temp1.convertToFahrenheit(32)

class Playlist:
    def __init__(self):
        self.songs = []
    def addSong(self, song):
        self.songs.append(song)
    def removeSong(self, song):
        if song in self.songs:
            self.songs.remove(song)
    def playPlaylist(self):
        print(self.songs)

myPlaylist = Playlist()

myPlaylist.addSong("War")
myPlaylist.addSong("Ghungroo")
myPlaylist.addSong("223's")

myPlaylist.playPlaylist()

myPlaylist.removeSong("Ghungroo")

myPlaylist.playPlaylist()