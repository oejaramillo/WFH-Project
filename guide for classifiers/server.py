from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a secret key for session management

# Initialize SQLite Database
def init_db():
    with sqlite3.connect('app.db') as db:
        db.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        age TEXT,
                        gender TEXT,
                        location TEXT)''')
        db.execute('''CREATE TABLE IF NOT EXISTS classifications (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        ad_text TEXT,
                        classification TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')

@app.route('/')
def index():
    return render_template('index.html')

# Add more routes for handling form submissions and classification

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
