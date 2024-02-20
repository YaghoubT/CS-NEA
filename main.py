import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    def __init__(self, master):
        super().__init__(master)
        self.current_index = 0
        self.total_records = get_total_records("stock")
        self.create_widgets()
        self.show_data()

    def create_widgets(self):
        labels = ["Item Code", "Item Name", "Quantity", "Cost Price", "Sell Price", "Date"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self, text=f"{label}:", font=("Arial", 14)).grid(row=i, column=0, padx=10, pady=2, sticky="w")
            entry = ttk.Entry(self, font=("Arial", 14), width=25)
            entry.grid(row=i, column=1, padx=10, pady=2, sticky="e")
            self.entries[label.lower().replace(" ", "_")] = entry

        button_texts = [("Add", self.add_stock), ("Edit", self.edit_stock), ("Delete", self.delete_stock), 
                        ("Clear", self.clear_entry_fields), ("Previous", self.show_previous), ("Next", self.show_next)]
        self.buttons = {}
        for i, (text, command) in enumerate(button_texts):
            button = ttk.Button(self, text=text, command=command)
            button.grid(row=6, column=i, padx=5, pady=10, sticky="ew")
            self.buttons[text.lower()] = button

        self.buttons["edit"].config(state="disabled")
        self.buttons["delete"].config(state="disabled")

        self.grid_columnconfigure(1, weight=1) 

    def add_stock(self):
        stock_data = {field: entry.get() for field, entry in self.entries.items()}
        add_record("stock", stock_data)
        self.total_records = get_total_records("stock")
        self.current_index = self.total_records - 1 
        self.show_data()
        self.clear_entry_fields()

    def edit_stock(self):
        if self.current_index >= 0 and self.current_index < self.total_records:
            stock_data = {field: entry.get() for field, entry in self.entries.items()}
            update_record_at_index("stock", self.current_index + 1, stock_data) 
            self.show_data()

    def delete_stock(self):
        if self.current_index >= 0 and self.current_index < self.total_records:
            confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this stock record?")
            if confirmation:
                delete_record_at_index("stock", self.current_index + 1) 
                self.total_records -= 1
                self.current_index = max(0, self.current_index - 1)
                self.show_data()

    def clear_entry_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.current_index = -1
        self.buttons["edit"].config(state="disabled")
        self.buttons["delete"].config(state="disabled")

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_data()

    def show_next(self):
        if self.current_index < self.total_records - 1:
            self.current_index += 1
            self.show_data()

    def show_data(self):
        if self.total_records > 0 and self.current_index >= 0:
            stock_data = get_record_at_index("stock", self.current_index)
            for field, entry in self.entries.items():
                entry.delete(0, tk.END)
                entry.insert(0, stock_data[field])
            self.buttons["edit"].config(state="normal")
            self.buttons["delete"].config(state="normal")
        else:
            self.clear_entry_fields()

def main():
    root = tk.Tk()
    root.title("Inventory Management System")

    login_window = LoginWindow(root)
    login_window.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()