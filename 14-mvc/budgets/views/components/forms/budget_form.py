from tkinter import ttk, StringVar, END
from datetime import datetime


class BudgetForm(ttk.Frame):

   def __init__(self, controller, view):
      super().__init__(view)
      self.controller = controller

      self.label_title = ttk.Label(self, text="Title", anchor="w", width=10)
      self.label_title.grid(row=0, column=0, sticky="nsew" ,padx=5, pady=5)

      self.entry_title = ttk.Entry(self, width=20)
      self.entry_title.grid(row=0, column=1, columnspan=2, sticky="nsew" ,padx=5, pady=5)

      self.label_type = ttk.Label(self, text="Type", anchor="w")
      self.label_type.grid(row=1, column=0, sticky="nsew" ,padx=5, pady=5)
      self.selected = StringVar(value="r")
      radio_button1 = ttk.Radiobutton(self, text="Income", variable=self.selected, value="r")
      radio_button1.grid(row=1, column=1, sticky="nsew",padx=5, pady=5)

      radio_button2 = ttk.Radiobutton(self, text="Expense", variable=self.selected, value="e")
      radio_button2.grid(row=1, column=2, sticky="nsew",padx=5, pady=5)

      self.label_amount =  ttk.Label(self, text="Amount", anchor="w")
      self.label_amount.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5, pady=5)

      self.spinbox_amount = ttk.Spinbox(self, from_=0, to=100000, width=20)
      self.spinbox_amount.grid(row=2, column=1, columnspan=2,sticky="nsew",padx=5, pady=5)

      self.submit_button = ttk.Button(self, text="Submit", command=lambda : self.submit_form())
      self.submit_button.grid(row=3, column=1, sticky="nsew",padx=5, pady=5)

      self.reset_button = ttk.Button(self, text="Reset", command=lambda : self.reset_form())
      self.reset_button.grid(row=3, column=2, sticky="nsew",padx=5, pady=5)

   def reset_form(self):
      self.entry_title.delete(0, END)
      self.spinbox_amount.delete(0, END)
      self.selected.set("r")

   def submit_form(self):
      formValues = (datetime.now(), self.entry_title.get(), self.selected.get(), self.spinbox_amount.get())
      self.controller.add_budget(formValues)
    
