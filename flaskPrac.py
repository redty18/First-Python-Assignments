from flask import Flask, request, jsonify

app = Flask(__name__)

class Book():
    def __init__(self, bookID, title, author, published_date, isbn, page_count, cover_image, language):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.published_date = published_date
        self.isbn = isbn
        self.page_count = page_count
        self.cover_image = cover_image
        self.language = language
    
    def update_Book(self, updatedBook):
        self.bookID = updatedBook.get("UpdatedBookID", self.bookID)
        self.title = updatedBook.get("UpdatedTitle", self.title)
        self.author = updatedBook.get("UpdatedAuthor", self.author)
        self.published_date = updatedBook.get("UpdatedPublishDate", self.published_date)
        self.isbn = updatedBook.get("UpdatedISBN", self.isbn)
        self.page_count = updatedBook.get("UpdatedPageCount", self.page_count)
        self.cover_image = updatedBook.get("UpdatedCoverImage", self.cover_image)
        self.language = updatedBook.get("UpdatedLanguage", self.language)

    def to_dict(self):
        return {
            "id": self.bookID,
            "title": self.title,
            "author": self.author,
            "published_date": self.published_date,
            "isbn": self.isbn,
            "page_count": self.page_count,
            "cover_image": self.cover_image,
            "language": self.language
        }
    
    def __str__(self):
        return f"ID: {self.bookID}, Title: {self.title}, Author: {self.author}, Published: {self.published_date}, ISBN: {self.isbn}, Page Count: {self.page_count}"

bookList = []

@app.route('/addbooks', methods=['POST'])
def createBook():
    data = request.get_json()
    bookID = data.get("BookID")
    bookTitle = data.get("BookTitle")
    bookAuthor = data.get("BookAuthor")
    publishDate = data.get("Published_Date")
    isbn = data.get("ISBN")
    pageCount = data.get("Page_Count")
    coverImage = data.get("Cover_Image")
    language = data.get("Language")
    for book in bookList:
        if book.bookID == bookID:
            return jsonify({"Error": "This ID already exists"}), 400
    
    book1 = Book(bookID=bookID, title=bookTitle, author=bookAuthor, published_date=publishDate, isbn=isbn, page_count=pageCount, cover_image=coverImage, language=language)
    bookList.append(book1)
    return jsonify(book1.to_dict()), 201

@app.route("/books", methods={'GET'})
def getBooks():
    books_json = [book.to_dict() for book in bookList]
    return jsonify({'Books': books_json}), 200

@app.route("/books/<int:book_ID>", methods=['GET'])
def getBooksbyID(book_ID):
    for book in bookList:
        if book.bookID == book_ID:
            return jsonify(book.to_dict()), 200
        else:
            return jsonify({"Error": "This ID doesn't exist."}), 404
        
@app.route("/updatebooks/<int:book_ID>", methods=['PUT'])
def updateBookbyID(book_ID):
    data = request.get_json()
    for book in bookList:
        if book.bookID == book_ID:
            book.update_Book(data)
            return jsonify(book.to_dict()), 200
        else:
            return jsonify({"Error": "This Book ID doesn't exist."}), 404

@app.route("/deletebooks/<int:book_ID>", methods=['DELETE'])
def deleteBookbyID(book_ID):
    for book in bookList:
        if book.bookID == book_ID:
            bookList.remove(book)
            return jsonify({"Message": "Book Deleted"}), 204
        else:
            return jsonify({"Error": "Book ID not found."}), 404
        
if __name__ == "__main__":
    app.run(debug=True)



