import sqlite3

def create_database():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            address TEXT,
            passport TEXT,
            date_joined TEXT,
            salary REAL,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_employee(first_name, last_name, age, address, passport, date_joined, salary, username, password):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO employees (first_name, last_name, age, address, passport, date_joined, salary, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (first_name, last_name, age, address, passport, date_joined, salary, username, password)
        cursor.execute(sql, values)
        conn.commit()
        print("Employee added successfully.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()