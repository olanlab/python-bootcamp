import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # create a treeview widget
        self.treeview = ttk.Treeview(self, columns=("Name", "Age", "Gender"), show="headings")

        # add column headings
        self.treeview.heading("Name", text="Name", command=lambda: self.sort_column("Name", False))
        self.treeview.heading("Age", text="Age", command=lambda: self.sort_column("Age", True))
        self.treeview.heading("Gender", text="Gender", command=lambda: self.sort_column("Gender", False))

        # add rows to the treeview
        self.treeview.insert("", "end", values=("John Doe", "35", "Male"))
        self.treeview.insert("", "end", values=("Jane Doe", "28", "Female"))
        self.treeview.insert("", "end", values=("Bob Smith", "42", "Male"))
        self.treeview.insert("", "end", values=("Alice Jones", "23", "Female"))

        # pack the treeview widget
        self.treeview.pack(padx=10, pady=10)

    def sort_column(self, column, reverse):
        """Sort treeview by a column"""
        data = [(self.treeview.set(child, column), child) for child in self.treeview.get_children("")]
        data.sort(reverse=reverse)

        # set sort symbol on column heading
        if reverse:
            self.treeview.heading(column, text=f"{column} ▼")
        else:
            self.treeview.heading(column, text=f"{column} ▲")

        # rearrange items in sorted positions
        for index, (value, child) in enumerate(data):
            self.treeview.move(child, "", index)

        # reverse sort direction
        self.treeview.heading(column, command=lambda: self.sort_column(column, not reverse))

root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()
