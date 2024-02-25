import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from database import *

create_database()

class LoginWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def authenticate_admin(self, username, password):
        valid_username = "admin"
        valid_password = "admin123"
        return username == valid_username and password == valid_password

    def authenticate_employee(self, username, password):
        valid_username = "employee"
        valid_password = "employee123"
        return username == valid_username and password == valid_password

    def login_clicked(self, user_type, username_entry, password_entry):
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if user_type == "admin":
            authenticated = self.authenticate_admin(entered_username, entered_password)
        elif user_type == "employee":
            authenticated = self.authenticate_employee(entered_username, entered_password)
        else:
            authenticated = False

        if authenticated:
            self.parent.destroy()

            if user_type == "admin":
                MainWindow(entered_username)
            elif user_type == "employee":
                pass
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_widgets(self):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        self.parent.geometry(f"{screen_width}x{screen_height}")

        frame = tk.Frame(self.parent, bg="lightgreen")
        frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(frame, bg="white", width=screen_width//2, height=screen_height)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(frame, bg="Green", width=screen_width//2, height=screen_height)
        right_frame.pack(side="left", fill="both", expand=True)

        label_username = tk.Label(left_frame, text="Username:", font=("Arial", 12))
        label_username.place(relx=0.2, rely=0.4, anchor=tk.W)

        username_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
        username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        label_password = tk.Label(left_frame, text="Password:", font=("Arial", 12))
        label_password.place(relx=0.2, rely=0.5, anchor=tk.W)

        password_entry = tk.Entry(left_frame, show="*", width=20, font=("Arial", 12))
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        admin_login_button = tk.Button(left_frame, text="Admin Login", command=lambda: self.login_clicked("admin", username_entry, password_entry), font=("Arial", 12))
        admin_login_button.place(relx=0.2, rely=0.6, anchor=tk.W)

        employee_login_button = tk.Button(left_frame, text="Employee Login", command=lambda: self.login_clicked("employee", username_entry, password_entry), font=("Arial", 12))
        employee_login_button.place(relx=0.5, rely=0.6, anchor=tk.W)

class MainWindow(tk.Tk):
    def __init__(self, username):
        super().__init__()

        self.title("Inventory Management System - " + username)
        self.state("zoomed")

        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 14), padding=10)

        self.side_panel = ttk.Frame(self, width=150, relief="raised", borderwidth=2)
        self.side_panel.pack(side="left", fill="y", padx=5, pady=5)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.create_buttons()
        self.create_tabs()
    
    def create_tabs(self):
        admin_dashboard_tab = ttk.Frame(self.notebook)
        employee_tab = EmployeeTab(self.notebook)  
        customers_tab = CustomerTab(self.notebook)
        stock_tab = StockTab(self.notebook)
        check_stock_tab = ttk.Frame(self.notebook)
        sales_tab = ttk.Frame(self.notebook)

        self.notebook.add(admin_dashboard_tab, text="Admin Dashboard")
        self.notebook.add(employee_tab, text="Employees") 
        self.notebook.add(customers_tab, text="Customers")
        self.notebook.add(stock_tab, text="Stock")
        self.notebook.add(check_stock_tab, text="Check Stock")
        self.notebook.add(sales_tab, text="Sales")

    def create_buttons(self):
        admin_dashboard_button = ttk.Button(self.side_panel, text="Admin Dashboard", command=lambda: self.show_tab(0))
        admin_dashboard_button.pack(pady=10, fill="x")

        employee_tab_button = ttk.Button(self.side_panel, text="Employees", command=lambda: self.show_tab(1))
        employee_tab_button.pack(pady=10, fill="x")

        customers_button = ttk.Button(self.side_panel, text="Customers", command=lambda: self.show_tab(2))
        customers_button.pack(pady=10, fill="x")

        stock_button = ttk.Button(self.side_panel, text="Stock", command=lambda: self.show_tab(3))
        stock_button.pack(pady=10, fill="x")

        check_stock_button = ttk.Button(self.side_panel, text="Check Stock", command=lambda: self.show_tab(4))
        check_stock_button.pack(pady=10, fill="x")

        sales_button = ttk.Button(self.side_panel, text="Sales", command=lambda: self.show_tab(5))
        sales_button.pack(pady=10, fill="x")


    def show_tab(self, index):
        self.current_index = index 
        self.notebook.select(index)

class EmployeeTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.current_index = 0
        self.total_records = 0 
        self.create_widgets()
        self.show_data()
        self.clear_entry_fields()
        
    def create_widgets(self):
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

        self.username_label = ttk.Label(self, text="Username:", font=("Arial", 14))
        self.username_entry = ttk.Entry(self, font=("Arial", 14))

        self.password_label = ttk.Label(self, text="Password:", font=("Arial", 14))
        self.password_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.prev_button, self.next_button, self.clear_button, self.add_button, self.edit_button, self.delete_button = self.create_buttons()
        
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

        self.username_label.pack(fill="x", padx=10, pady=5)
        self.username_entry.pack(fill="x", padx=10, pady=5)

        self.password_label.pack(fill="x", padx=10, pady=5)
        self.password_entry.pack(fill="x", padx=10, pady=5)
        
        self.prev_button.pack(fill="x", padx=10, pady=5, side="left")
        self.next_button.pack(fill="x", padx=10, pady=5, side="right")
        
        self.add_button.pack(fill="x", padx=10, pady=(5, 10))
        self.clear_button.pack(fill="x", padx=10, pady=(10, 15))
        self.edit_button.pack(fill="x", padx=10, pady=(20, 25))
        self.delete_button.pack(fill="x", padx=10, pady=(30, 35))

        self.pack(expand=True, fill="both")
    
    def create_buttons(self):
        prev_button = ttk.Button(self, text="Previous", command=self.show_previous, style="TButton")
        next_button = ttk.Button(self, text="Next", command=self.show_next, style="TButton")
        clear_button = ttk.Button(self, text="Clear", command=self.clear_entry_fields, style="TButton")
        add_button = ttk.Button(self, text="Add", command=self.add_employee, style="TButton")
        edit_button = ttk.Button(self, text="Edit", command=self.edit_employee, style="TButton", state="disabled")
        delete_button = ttk.Button(self, text="Delete", command=self.delete_employee, style="TButton", state="disabled")

        return prev_button, next_button, clear_button, add_button, edit_button, delete_button
        
    def add_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        passport = self.passport_entry.get()
        date_joined = self.date_joined_entry.get()
        salary = self.salary_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        add_record("employees", {"first_name": first_name, "last_name": last_name, "age": age, "address": address, "passport": passport, "date_joined": date_joined, "salary": salary, "username": username, "password": password})

        self.show_data()
        self.clear_entry_fields()
    
    def edit_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        passport = self.passport_entry.get()
        date_joined = self.date_joined_entry.get()
        salary = self.salary_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        update_record_at_index("employees", self.current_index, {"first_name": first_name, "last_name": last_name, "age": age, "address": address, "passport": passport, "date_joined": date_joined, "salary": salary, "username": username, "password": password})

        self.show_data()
    
    def delete_employee(self):
        if self.total_records > 0:
            confirmation = messagebox.askyesno("Delete Employee", "Are you sure you want to delete this employee?")
            if confirmation:
                delete_record_at_index("employees", self.current_index)
                self.total_records = get_total_records("employees")
                if self.current_index < self.total_records:
                    self.show_data()
                else:
                    self.clear_entry_fields()

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_data()
            self.add_button.config(state="disabled")
         

    def show_next(self):
        if self.current_index < self.total_records - 1:
            self.current_index += 1
            self.show_data()
            self.add_button.config(state="disabled") 

    def show_data(self):
        self.total_records = get_total_records("employees")
        if self.total_records > 0:
            employee_data = get_record_at_index("employees", self.current_index)
            if employee_data:
                self.populate_fields(employee_data)
                self.delete_button.config(state="normal")
                self.edit_button.config(state="normal") 
            else:
                self.clear_entry_fields() 
                self.delete_button.config(state="disabled")
                self.edit_button.config(state="disabled") 
        else:
            self.clear_entry_fields() 
            self.delete_button.config(state="disabled")
            self.edit_button.config(state="disabled")

    def populate_fields(self, data):
        self.first_name_entry.delete(0, tk.END)
        self.first_name_entry.insert(0, data.get("first_name", ""))

        self.last_name_entry.delete(0, tk.END)
        self.last_name_entry.insert(0, data.get("last_name", ""))

        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, data.get("age", ""))

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, data.get("address", ""))

        self.passport_entry.delete(0, tk.END)
        self.passport_entry.insert(0, data.get("passport", ""))

        self.date_joined_entry.delete(0, tk.END)
        self.date_joined_entry.insert(0, data.get("date_joined", ""))

        self.salary_entry.delete(0, tk.END)
        self.salary_entry.insert(0, data.get("salary", ""))

        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, data.get("username", ""))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, data.get("password", ""))

    def clear_entry_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.passport_entry.delete(0, tk.END)
        self.date_joined_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.add_button.config(state="normal") 
        self.delete_button.config(state="disabled")
        self.edit_button.config(state="disabled")

class CustomerTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.current_index = 0
        self.total_records = 0 
        self.create_widgets()
        self.show_data()
        self.clear_entry_fields()
 
    def create_widgets(self):
        self.company_name_label = ttk.Label(self, text="Company Name:", font=("Arial", 14))
        self.company_name_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.location_label = ttk.Label(self, text="Location:", font=("Arial", 14))
        self.location_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.mobile_label = ttk.Label(self, text="Mobile:", font=("Arial", 14))
        self.mobile_entry = ttk.Entry(self, font=("Arial", 14))
        
        self.email_label = ttk.Label(self, text="Email:", font=("Arial", 14))
        self.email_entry = ttk.Entry(self, font=("Arial", 14))

        self.prev_button, self.next_button, self.clear_button, self.add_button, self.edit_button, self.delete_button = self.create_buttons()
        
        self.company_name_label.pack(fill="x", padx=10, pady=(10, 5))
        self.company_name_entry.pack(fill="x", padx=10, pady=5)
        
        self.location_label.pack(fill="x", padx=10, pady=5)
        self.location_entry.pack(fill="x", padx=10, pady=5)
        
        self.mobile_label.pack(fill="x", padx=10, pady=5)
        self.mobile_entry.pack(fill="x", padx=10, pady=5)
        
        self.email_label.pack(fill="x", padx=10, pady=5)
        self.email_entry.pack(fill="x", padx=10, pady=5)
        
        self.prev_button.pack(fill="x", padx=10, pady=5, side="left")
        self.next_button.pack(fill="x", padx=10, pady=5, side="right")
        
        self.add_button.pack(fill="x", padx=10, pady=(5, 10))
        self.clear_button.pack(fill="x", padx=10, pady=(10, 15))
        self.edit_button.pack(fill="x", padx=10, pady=(20, 25))
        self.delete_button.pack(fill="x", padx=10, pady=(30, 35))

        self.pack(expand=True, fill="both")
    
    def create_buttons(self):
        prev_button = ttk.Button(self, text="Previous", command=self.show_previous, style="TButton")
        next_button = ttk.Button(self, text="Next", command=self.show_next, style="TButton")

        clear_button = ttk.Button(self, text="Clear", command=self.clear_entry_fields, style="TButton")
        add_button = ttk.Button(self, text="Add", command=self.add_customer, style="TButton")
        edit_button = ttk.Button(self, text="Edit", command=self.edit_customer, style="TButton", state="disabled")
        delete_button = ttk.Button(self, text="Delete Customer", command=self.delete_customer, style="TButton", state="disabled")

        return prev_button, next_button, clear_button, add_button, edit_button, delete_button
        
    def add_customer(self):
        company_name = self.company_name_entry.get()
        location = self.location_entry.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()

        add_record("customers", {"company_name": company_name, "location": location, "mobile": mobile, "email": email})
        self.show_data()
        self.clear_entry_fields()
    
    def edit_customer(self):
        company_name = self.company_name_entry.get()
        location = self.location_entry.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()

        update_record_at_index("customers", self.current_index, {"company_name": company_name, "location": location, "mobile": mobile, "email": email})

        self.show_data()
    
    def delete_customer(self):
        if self.total_records > 0:
            confirmation = messagebox.askyesno("Delete Customer", "Are you sure you want to delete this customer?")
            if confirmation:
                delete_record_at_index("customers", self.current_index)
                self.total_records = get_total_records("customers")
                if self.current_index < self.total_records:
                    self.show_data()
                else:
                    self.clear_entry_fields()

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_data()
            self.add_button.config(state="disabled") 

    def show_next(self):
        if self.current_index < self.total_records - 1:
            self.current_index += 1
            self.show_data()
            self.add_button.config(state="disabled") 

    def show_data(self):
        self.total_records = get_total_records("customers")
        if self.total_records > 0:
            customer_data = get_record_at_index("customers", self.current_index)
            if customer_data:
                self.populate_fields(customer_data)
                self.delete_button.config(state="normal")
                self.edit_button.config(state="normal") 
            else:
                self.clear_entry_fields() 
                self.delete_button.config(state="disabled")
                self.edit_button.config(state="disabled") 
        else:
            self.clear_entry_fields() 
            self.delete_button.config(state="disabled")
            self.edit_button.config(state="disabled")

    def populate_fields(self, data):
        self.company_name_entry.delete(0, tk.END)
        self.company_name_entry.insert(0, data.get("company_name", ""))  
        self.location_entry.delete(0, tk.END)
        self.location_entry.insert(0, data.get("location", ""))
        self.mobile_entry.delete(0, tk.END)
        self.mobile_entry.insert(0, data.get("mobile", ""))
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, data.get("email", ""))

    def clear_entry_fields(self):
        self.company_name_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.add_button.config(state="normal") 
        self.delete_button.config(state="disabled")
        self.edit_button.config(state="disabled")

class StockTab(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.records_per_page = 10
        self.current_page = 0
        self.total_records = get_total_records("stock")
        self.selected_item = None
        self.initialize_ui()
        self.populate_table()

    def initialize_ui(self):
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row=0, column=0, padx=10, pady=10)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Item Code", "Item Name", "Quantity", "Cost Price", "Sell Price"), show="headings")
        for col in ["Item Code", "Item Name", "Quantity", "Cost Price", "Sell Price"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.entry_frame = ttk.Frame(self)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=5)

        self.entry_fields = ["Item Code", "Item Name", "Quantity", "Cost Price", "Sell Price"]
        self.entries = {}
        for idx, field in enumerate(self.entry_fields):
            ttk.Label(self.entry_frame, text=field).grid(row=0, column=idx)
            self.entries[field] = ttk.Entry(self.entry_frame)
            self.entries[field].grid(row=1, column=idx)

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0, padx=10, pady=5)

        self.submit_button = ttk.Button(self.button_frame, text="Add Record", command=self.add_record)
        self.submit_button.grid(row=0, column=0, padx=5, pady=5)

        self.edit_button = ttk.Button(self.button_frame, text="Edit Selected Record", command=self.edit_record)
        self.edit_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Selected Record", command=self.delete_record)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.clear_button = ttk.Button(self.button_frame, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=0, column=3, padx=5, pady=5)

        self.navigation_frame = ttk.Frame(self)
        self.navigation_frame.grid(row=3, column=0, padx=10, pady=5)

        self.prev_button = ttk.Button(self.navigation_frame, text="Previous", command=self.prev_page)
        self.prev_button.grid(row=0, column=0, padx=5, pady=5)

        self.next_button = ttk.Button(self.navigation_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=0, column=1, padx=5, pady=5)

        self.tree.bind('<<TreeviewSelect>>', self.on_item_selected)

    def on_item_selected(self, event):
        selected = self.tree.selection()
        if selected:
            self.selected_item = selected[0]
            record = self.tree.item(self.selected_item)['values']
            for i, key in enumerate(self.entry_fields):
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, record[i])

    def populate_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        start = self.current_page * self.records_per_page
        end = start + self.records_per_page
        for i in range(start, min(end, self.total_records)):
            record = get_record_at_index("stock", i)
            if record:
                self.tree.insert('', 'end', values=(record['item_code'], record['item_name'], record['quantity'], record['cost_price'], record['sell_price']))

    def add_record(self):
        record_data = {
            'item_code': self.entries['Item Code'].get(),
            'item_name': self.entries['Item Name'].get(),
            'quantity': self.entries['Quantity'].get(),
            'cost_price': self.entries['Cost Price'].get(),
            'sell_price': self.entries['Sell Price'].get()
        }
        try:
            add_stock(
                record_data['item_code'], 
                record_data['item_name'], 
                record_data['quantity'], 
                record_data['cost_price'], 
                record_data['sell_price']
            )
            self.total_records = get_total_records("stock")
            self.populate_table()
            messagebox.showinfo("Success", "Record added successfully")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add record: {e}")

    def edit_record(self):
        if not self.selected_item:
            messagebox.showerror("Error", "No record selected")
            return
        selected_record = self.tree.item(self.selected_item)['values']
        item_code = selected_record[0]
        record_data = {
            'item_name': self.entries['Item Name'].get(),
            'quantity': self.entries['Quantity'].get(),
            'cost_price': self.entries['Cost Price'].get(),
            'sell_price': self.entries['Sell Price'].get()
        }
        try:
            update_stock(item_code, record_data)
            self.populate_table()
            messagebox.showinfo("Success", "Record updated successfully")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update record: {e}")

    def delete_record(self):
        if not self.selected_item:
            messagebox.showerror("Error", "No record selected")
            return
        selected_record = self.tree.item(self.selected_item)['values']
        item_code = selected_record[0]
        response = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
        if response:
            try:
                delete_stock(item_code)
                self.populate_table()
                messagebox.showinfo("Success", "Record deleted successfully")
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete record: {e}")

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.selected_item = None

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.populate_table()

    def next_page(self):
        if (self.current_page + 1) * self.records_per_page < self.total_records:
            self.current_page += 1
            self.populate_table()

def main(): 
    root = tk.Tk()
    root.title("Inventory Management System")

    login_window = LoginWindow(root)
    login_window.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()