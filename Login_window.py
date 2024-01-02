import tkinter as tk
from tkinter import messagebox
from main_window import open_main_window

def authenticate_admin(username, password):
    # Replace this with your actual admin authentication logic
    valid_username = "admin"
    valid_password = "admin123"
    return username == valid_username and password == valid_password

def authenticate_employee(username, password):
    # Replace this with your actual employee authentication logic
    valid_username = "employee"
    valid_password = "employee123"
    return username == valid_username and password == valid_password

def login_clicked(user_type, username_entry, password_entry, login_window):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if user_type == "admin":
        authenticated = authenticate_admin(entered_username, entered_password)
    elif user_type == "employee":
        authenticated = authenticate_employee(entered_username, entered_password)
    else:
        authenticated = False

    if authenticated:
        open_main_window(login_window, entered_username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def create_login_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    frame = tk.Frame(root, bg="lightgreen")
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

    admin_login_button = tk.Button(left_frame, text="Admin Login", command=lambda: login_clicked("admin", username_entry, password_entry, root), font=("Arial", 12))
    admin_login_button.place(relx=0.2, rely=0.6, anchor=tk.W)

    employee_login_button = tk.Button(left_frame, text="Employee Login", command=lambda: login_clicked("employee", username_entry, password_entry, root), font=("Arial", 12))
    employee_login_button.place(relx=0.5, rely=0.6, anchor=tk.W)