import tkinter as tk
from Login_window import create_login_window

def main():
    root = tk.Tk()
    root.title("Inventory Management System")

    create_login_window(root)

    root.mainloop()

if __name__ == "__main__":
    main()