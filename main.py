import tkinter as tk
from login_window import LoginWindow

def main():
    root = tk.Tk()
    root.title("Inventory Management System")

    login_window = LoginWindow(root)
    login_window.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
