import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        filter_frame = tk.Frame(self)
        filter_frame.pack(padx=10, pady=10)

        name_label = tk.Label(filter_frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(filter_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        age_label = tk.Label(filter_frame, text="Age:")
        age_label.grid(row=1, column=0, sticky="e")
        self.age_entry = tk.Entry(filter_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        gender_label = tk.Label(filter_frame, text="Gender:")
        gender_label.grid(row=2, column=0, sticky="e")
        self.gender_combobox = ttk.Combobox(filter_frame, values=["Male", "Female"])
        self.gender_combobox.grid(row=2, column=1, padx=5, pady=5)

        filter_button = tk.Button(filter_frame, text="Filter", command=self.filter_data)
        filter_button.grid(row=3, column=1, padx=5, pady=5)

        clear_button = tk.Button(filter_frame, text="Clear", command=self.clear_filter)
        clear_button.grid(row=3, column=0, padx=5, pady=5)

        self.treeview = ttk.Treeview(self, columns=("Name", "Age", "Gender"), show="headings")
        
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Age", text="Age")
        self.treeview.heading("Gender", text="Gender")

        
        self.treeview.insert("", "end", values=("John Doe", "35", "Male"))
        self.treeview.insert("", "end", values=("Jane Doe", "28", "Female"))
        self.treeview.insert("", "end", values=("Bob Smith", "42", "Male"))
        self.treeview.insert("", "end", values=("Alice Jones", "23", "Female"))

        
        self.treeview.pack(padx=10, pady=10)

    def filter_data(self):
        """Filter the data in the treeview based on the filter criteria"""
        self.clear_filter()

        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()

        
        for child in self.treeview.get_children():
            values = self.treeview.item(child)["values"]
            if (not name or name.lower() in str(values[0]).lower()) \
                    and (not age or age == str(values[1])) \
                    and (not gender or gender == values[2]):
                self.treeview.selection_add(child)

    def clear_filter(self):
        """Clear any previous filters"""
        for child in self.treeview.selection():
            self.treeview.selection_remove(child)

root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()
