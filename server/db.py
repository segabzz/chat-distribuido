import sqlite3

def init_db():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        message TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()
    
    add_default_users()

def add_default_users():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("sergio", "1234"))
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin"))
    
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    conn.close()
    return user is not None

def save_message(username, message):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))

    conn.commit()
    conn.close()
