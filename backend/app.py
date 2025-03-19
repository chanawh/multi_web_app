from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'mydb'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return connection

@app.route('/')
def hello_world():
    return "Hello, World! Welcome to the Flask backend."

@app.route('/users')
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, username, email FROM users;')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    
    # Return the users as JSON
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
