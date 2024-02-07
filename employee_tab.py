import tkinter as tk
from tkinter import ttk
import sqlite3

class EmployeeTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.current_index = 0
        self.employees = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.conn = sqlite3.connect("employees.db")
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                address TEXT,
                passport TEXT,
                date_joined TEXT,
                salary REAL
            )
        """)
        
        self.first_name_label = ttk.Label(self, text="First Name:", font=("Arial", 14))
        self.first_name_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.last_name_label = ttk.Label(self, text="Last Name:", font=("Arial", 14))
        self.last_name_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.age_label = ttk.Label(self, text="Age:", font=("Arial", 14))
        self.age_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.address_label = ttk.Label(self, text="Address:", font=("Arial", 14))
        self.address_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.passport_label = ttk.Label(self, text="Passport Number:", font=("Arial", 14))
        self.passport_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.date_joined_label = ttk.Label(self, text="Date Joined:", font=("Arial", 14))
        self.date_joined_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.salary_label = ttk.Label(self, text="Salary:", font=("Arial", 14))
        self.salary_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.prev_button = ttk.Button(self, text="Previous", command=self.show_previous, style="TButton")
        self.next_button = ttk.Button(self, text="Next", command=self.show_next, style="TButton")
        
        self.add_button = ttk.Button(self, text="Add Employee", command=self.add_employee, style="TButton")
        
        self.first_name_label.pack(fill="x", padx=10, pady=(10, 5))
        self.first_name_entry.pack(fill="x", padx=10, pady=5)
        
        self.last_name_label.pack(fill="x", padx=10, pady=5)
        self.last_name_entry.pack(fill="x", padx=10, pady=5)
        
        self.age_label.pack(fill="x", padx=10, pady=5)
        self.age_entry.pack(fill="x", padx=10, pady=5)
        
        self.address_label.pack(fill="x", padx=10, pady=5)
        self.address_entry.pack(fill="x", padx=10, pady=5)
        
        self.passport_label.pack(fill="x", padx=10, pady=5)
        self.passport_entry.pack(fill="x", padx=10, pady=5)
        
        self.date_joined_label.pack(fill="x", padx=10, pady=5)
        self.date_joined_entry.pack(fill="x", padx=10, pady=5)
        
        self.salary_label.pack(fill="x", padx=10, pady=5)
        self.salary_entry.pack(fill="x", padx=10, pady=5)
        
        self.prev_button.pack(fill="x", padx=10, pady=5, side="left")
        self.next_button.pack(fill="x", padx=10, pady=5, side="right")
        
        self.add_button.pack(fill="x", padx=10, pady=(5, 10))
        
        self.pack(expand=True, fill="both")
        
    def add_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        passport = self.passport_entry.get()
        date_joined = self.date_joined_entry.get()
        salary = self.salary_entry.get()
        
        try:
            sql = "INSERT INTO employees (first_name, last_name, age, address, passport, date_joined, salary) VALUES (?, ?, ?, ?, ?, ?, ?)"
            values = (first_name, last_name, age, address, passport, date_joined, salary)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Employee added successfully.")
        except Exception as e:
            print("Error:", e)
            self.conn.rollback()

        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.passport_entry.delete(0, tk.END)
        self.date_joined_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

    def show_previous(self):
        pass
        
    def show_next(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Employee Tab")
    
    employee_tab = EmployeeTab(root)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - root.winfo_reqwidth()) // 2
    y = (screen_height - root.winfo_reqheight()) // 2
    
    root.geometry(f"400x400+{x}+{y}")
    
    root.mainloop()

