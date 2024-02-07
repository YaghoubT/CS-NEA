import tkinter as tk
from tkinter import ttk
import sqlite3
from employee_tab import EmployeeTab  

class MainWindow(tk.Tk):
    def __init__(self, username):
        super().__init__()

        self.title("Inventory Management System - Welcome " + username)
        self.state("zoomed")

        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 14), padding=10)

        self.side_panel = ttk.Frame(self, width=150, relief="raised", borderwidth=2)
        self.side_panel.pack(side="left", fill="y", padx=5, pady=5)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.create_buttons()
        self.create_tabs()

    def create_buttons(self):
        admin_dashboard_button = ttk.Button(self.side_panel, text="Admin Dashboard", command=lambda: self.show_tab(0))
        admin_dashboard_button.pack(pady=10, fill="x")

        employee_tab_button = ttk.Button(self.side_panel, text="Employee Tab", command=lambda: self.show_tab(1))
        employee_tab_button.pack(pady=10, fill="x")

        input_customers_button = ttk.Button(self.side_panel, text="Input Customers", command=lambda: self.show_tab(2))
        input_customers_button.pack(pady=10, fill="x")

        input_sales_button = ttk.Button(self.side_panel, text="Input Sales", command=lambda: self.show_tab(3))
        input_sales_button.pack(pady=10, fill="x")

        invoice_button = ttk.Button(self.side_panel, text="Invoice", command=lambda: self.show_tab(4))
        invoice_button.pack(pady=10, fill="x")

        enter_products_button = ttk.Button(self.side_panel, text="Enter Products", command=lambda: self.show_tab(5))
        enter_products_button.pack(pady=10, fill="x")

        check_stock_button = ttk.Button(self.side_panel, text="Check Stock", command=lambda: self.show_tab(6))
        check_stock_button.pack(pady=10, fill="x")

    def create_tabs(self):
        admin_dashboard_tab = ttk.Frame(self.notebook)
        employee_tab = EmployeeTab(self.notebook)  
        input_customers_tab = ttk.Frame(self.notebook)
        input_sales_tab = ttk.Frame(self.notebook)
        invoice_tab = ttk.Frame(self.notebook)
        enter_products_tab = ttk.Frame(self.notebook)
        check_stock_tab = ttk.Frame(self.notebook)

        self.notebook.add(admin_dashboard_tab, text="Admin Dashboard")
        self.notebook.add(employee_tab, text="Employee Tab")
        self.notebook.add(input_customers_tab, text="Input Customers")
        self.notebook.add(input_sales_tab, text="Input Sales")
        self.notebook.add(invoice_tab, text="Invoice")
        self.notebook.add(enter_products_tab, text="Enter Products")
        self.notebook.add(check_stock_tab, text="Check Stock")

        admin_dashboard_label = tk.Label(admin_dashboard_tab, text="Admin Dashboard Content", font=("Arial", 18))
        admin_dashboard_label.pack(pady=20)

        self.populate_admin_dashboard(admin_dashboard_tab)
    
    def populate_admin_dashboard(self, tab):
        query = "SELECT * FROM admin_dashboard_table"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        for row in data:
            label = tk.Label(tab, text=row, font=("Arial", 12))
            label.pack()

    def show_tab(self, index):
        self.notebook.select(index)

if __name__ == "__main__":
    main_window = MainWindow("TestUser")
    main_window.mainloop()
