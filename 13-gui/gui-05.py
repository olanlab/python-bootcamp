import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def show_info():
    messagebox.showinfo("Information", "This is an info message!")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error():
    messagebox.showerror("Error", "This is an error message!")

btn_info = tk.Button(root, text="Info", command=show_info)
btn_warning = tk.Button(root, text="Warning", command=show_warning)
btn_error = tk.Button(root, text="Error", command=show_error)


btn_info.pack(pady=10)
btn_warning.pack(pady=10)
btn_error.pack(pady=10)

root.mainloop()
