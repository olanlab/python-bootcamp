import tkinter as tk
from tkinter import ttk

class App(tk.Frame):

    data = [("John Doe", "35", "Male"), ("Jane Doe", "28", "Female"), ("Bob Smith", "42", "Male"), ("Alice Jones", "23", "Female")]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # create a treeview widget
        self.treeview = ttk.Treeview(self, columns=("Name", "Age", "Gender"), show="tree headings")

        self.radio_state = tk.IntVar()
        self.radioMale = ttk.Radiobutton(text="Radiobutton 1", value=1, variable=self.radio_state, command=self.on_radio)
        self.radioMale.pack()
        

        # define column headings
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Age", text="Age")
        self.treeview.heading("Gender", text="Gender")

        # add rows to the treeview
        for row in self.data:
            self.treeview.insert("", "end", values=row)

        # bind the treeview select event to a callback function
        self.treeview.bind("<<TreeviewSelect>>", self.on_select)

        # pack the treeview widget
        self.treeview.pack(padx=10, pady=10)

    def on_select(self, event):
        """Retrieve the data from the selected row"""
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item)["values"]
        print(values)

    def on_radio(self):

        print(self.radio_state.get())

root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()
