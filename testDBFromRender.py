from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
databaseURL = 'postgres://pythondb_iw2a_user:6cg6JvD2DQPKrumpT0Sj12wLmoVHP4wR@dpg-cmg1h66n7f5s73cb3c1g-a.oregon-postgres.render.com/pythondb_iw2a'
# Connect to PostgreSQL using the provided URL
conn = psycopg2.connect(databaseURL)


# Set up a cursor
cursor = conn.cursor()


# Create a 'users' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL
    )
""")
conn.commit()

# Insert sample data if the table is empty
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("INSERT INTO users (username) VALUES (%s), (%s), (%s)",
                   ('Adit', 'Myk', 'Alice'))
    conn.commit()


@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify({'users': users})

@app.route('/users', methods=['POST'])
def get_Username():
    # cursor.execute("SELECT username FROM users")
    # username = cursor.fetchall()
    data = request.get_json()
    name = data.get("username")
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (name,))
    return jsonify({'name' : name}), 201

@app.route('/users/<string:username>', methods=['GET'])
def getUsersAndName(username):
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    usernames = cursor.fetchone()
    if usernames == None:
        return jsonify({"Message" : "Username doesn't exist, please choose another one."}), 404
    else:
        return jsonify({"usernames" : usernames})

@app.route('/users/<username>', methods=['POST'])
def getUsername():
    cursor.execute("SELECT * FROM users WHERE ")


if __name__ == '__main__':
    app.run(debug=True)
