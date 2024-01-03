class bookInventory:
    def __init__(self):
        self.books = []

    def add_books(self, title, author):
        book = {"Title" : title, "Author" : author}
        self.books.append(book)
    
    def remove_books(self, title):
        for book in self.books:
            if book["Title"] == title:
                self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

list1 = bookInventory()
list1.add_books("The Iron Trial","Cassandra Clare")
list1.add_books("The Silver Trial","Cassandra Clare")
list1.add_books("The Gold Trial","Cassandra Clare")
list1.add_books("The Diamond Trial","Cassandra Clare")

list1.remove_books("The Silver Trial")

list1.display_books()