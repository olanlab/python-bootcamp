import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        
        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Tab 1")
        self.notebook.add(self.frame2, text="Tab 2")

        tk.Label(self.frame1, text="This is Tab 1").pack(pady=10)
        tk.Label(self.frame2, text="This is Tab 2").pack(pady=10)

        self.notebook.pack(padx=10, pady=10)

root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()
