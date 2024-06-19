# text = open("newPhile.txt", "r")
# newDict = dict()

# for line in text:
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")
#     for word in words:
#         if word in newDict:
#             newDict[word] = newDict[word] + 1
#         else:
#             newDict[word] = 1

# for key in list(newDict.keys()): 
#     print(key, ":", newDict[key]) 


# def checkAnagram(string1, string2):
#     string1 = string1.lower()
#     string2 = string2.lower()
#     return sorted(string1) == sorted(string2)

# print(checkAnagram("Listen", "silent")

# def transposeMatrix(matrix):
#     for list in matrix:

# matrix1 = [[1,2],[3,4],[5,6]]

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def areaCalc(self):
#         return self.length * self.width
    
#     def perimeterCalc(self):
#         return (self.length * 2) + (self.width * 2)

# newRectangle = Rectangle(25,10)
# print(newRectangle.areaCalc())
# print(newRectangle.perimeterCalc())

# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Error")

# class Book:
#     def __init__(self, title, author, ISBN):
#         self.title = title
#         self.author = author
#         self.ISBN = ISBN
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}"
    
# class Library:
#     def __init__(self):
#         self.books = []
    
#     def addBooks(self, book):
#         self.books.append(book)

#     def removeBooks(self, ISBN):
#         for book in self.books:
#             if book.ISBN == ISBN:
#                 self.books.remove(book)

#     def listBooks(self):
#         for book in self.books:
#             print(book, end=" ")

# newLibrary = Library()

# newLibrary.addBooks(Book('Title1', 'Author1', 'ISBN1'))
# newLibrary.addBooks(Book('Title2', 'Author2', 'ISBN2'))
# newLibrary.addBooks(Book('Title3', 'Author3', 'ISBN3'))
# newLibrary.addBooks(Book('Title4', 'Author4', 'ISBN4'))

# newLibrary.removeBooks('ISBN1')

# newLibrary.listBooks()