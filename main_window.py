import tkinter as tk

def open_main_window(login_window, username):
    login_window.destroy()

    main_window = tk.Tk()
    main_window.title("Welcome " + username)
    main_window.state("zoomed")


    main_window.mainloop()
