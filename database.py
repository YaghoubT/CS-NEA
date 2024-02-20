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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            location TEXT,
            mobile TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY,
        item_code TEXT,
        item_name TEXT,
        quantity INTEGER,
        cost_price REAL,
        sell_price REAL,
        date TEXT             
        )
    """)
    conn.commit()
    conn.close()

def add_record(table_name, record_data):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    field_names = ', '.join(record_data.keys())
    placeholders = ', '.join(['?'] * len(record_data))
    sql = f"INSERT INTO {table_name} ({field_names}) VALUES ({placeholders})"
    cursor.execute(sql, tuple(record_data.values()))
    conn.commit()
    conn.close()

def get_record_at_index(table_name, index):
    try:
        conn = sqlite3.connect("database")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1 OFFSET ?", (index,))
        data = cursor.fetchone()

        conn.close()

        if data:
            if table_name == "employees":
                keys = ['id', 'first_name', 'last_name', 'age', 'address', 'passport', 'date_joined', 'salary', 'username', 'password']
            elif table_name == "customers":
                keys = ['id', 'company_name', 'location', 'mobile', 'email']
            elif table_name == "stock":
                keys = ['id', 'item_code', 'item_name', 'quantity', 'cost_price', 'sell_price', 'date']
            else:
                print(f"Unknown table: {table_name}")
                return None
            return dict(zip(keys, data))
        else:
            print(f"No record found in table {table_name} at index {index}")
            return None
    except Exception as e:
        print(f"Error occurred while fetching record from table {table_name} at index {index}: {e}")
        return None

def get_total_records(table_name):
    conn = sqlite3.connect('database')
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_records = cursor.fetchone()[0]
    conn.close()
    return total_records

def delete_record_at_index(table_name, index):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (index + 1,))  
    conn.commit()
    conn.close()

def update_record_at_index(table_name, index, record_data):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    set_values = ', '.join([f"{field} = ?" for field in record_data.keys()])
    sql = f"""UPDATE {table_name} SET {set_values} WHERE id = ?"""
    cursor.execute(sql, tuple(record_data.values()) + (index + 1,))
    conn.commit()
    conn.close()