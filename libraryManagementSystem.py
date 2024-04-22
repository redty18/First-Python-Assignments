from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
databaseURL = 'postgres://pythondb_iw2a_user:6cg6JvD2DQPKrumpT0Sj12wLmoVHP4wR@dpg-cmg1h66n7f5s73cb3c1g-a.oregon-postgres.render.com/pythondb_iw2a'

# Connect to Database
conn = psycopg2.connect(databaseURL)

# Cursor Setup
cursor = conn.cursor()

# Table Creation
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            author VARCHAR(50) NOT NULL,
            publication_year INT,
            quantity INT   
    )
""")

# Add Data to the Table
cursor.execute('SELECT COUNT(*) FROM books')
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("INSERT INTO books (title, author, publication_year, quantity) VALUES (%s,%s,%s,%s)", 
                   ("The Iron Trial", "Cassandra Clare", 2016, 2))
    conn.commit()

@app.route('/books', methods=['GET'])
def getBooks():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return jsonify({'books' : books})

@app.route('/addbooks', methods=['POST'])
def addBook():
    data = request.get_json()
    bookID = data.get("id")
    bookName = data.get("title")
    bookAuthor = data.get("author")
    pubYear = data.get("publication_year")
    bookQuantity = data.get("quantity")
    cursor.execute("INSERT INTO books VALUES (%s,%s,%s,%s,%s)", (bookID, bookName, bookAuthor, pubYear, bookQuantity))
    return jsonify({"bookID" : bookID, "bookName" : bookName, "bookAuthor" : bookAuthor, "pubYear" : pubYear, "bookQuantity" : bookQuantity}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def getBookByID(book_id):
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if book == None:
        return jsonify({"Message" : "The ID doesn't exist, please choose another"}), 404
    else:
        return jsonify({"Book" : book})

@app.route('/updatebooks/<int:book_id>', methods=['PUT'])
def updateBook(book_id):
    data = request.get_json()
    bookName = data.get("title")
    bookAuthor = data.get("author")
    pubYear = data.get("publication_year")
    bookQuantity = data.get("quantity")
    cursor.execute("UPDATE books SET title = %s, author = %s, publication_year = %s, quantity = %s WHERE id = %s", (bookName, bookAuthor, pubYear, bookQuantity, book_id))
    return jsonify({"bookID" : book_id, "bookName" : bookName, "bookAuthor" : bookAuthor, "pubYear" : pubYear, "bookQuantity" : bookQuantity}), 201

@app.route('/deletebooks/<int:book_id>', methods=['DELETE'])
def deleteBook(book_id):
    cursor.execute("DELETE FROM books WHERE id = %s RETURNING id, title, author, publication_year, quantity", (book_id,))
    return jsonify({"Message" : "Book was Deleted!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
