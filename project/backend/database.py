import sqlite3
conn = sqlite3.connect(
    "taskmanager.db",
    check_same_thread=False
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    username TEXT,
    description TEXT,
    priority TEXT,
    due_date TEXT,
    completed INTEGER DEFAULT 0
)
""")
conn.commit()