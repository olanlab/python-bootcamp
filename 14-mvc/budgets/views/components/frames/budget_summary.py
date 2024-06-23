from tkinter import ttk



class BudgetSummaryFrame(ttk.Frame):

    def __init__(self, controller, view):
        super().__init__(view)
        self.controller = controller


        self.label_name = ttk.Label(self, text=f"{self.controller.app.user[3]} {self.controller.app.user[4]}", anchor="w", font=("Helvetica", 20))
        self.label_name.grid(row=0, column=0, sticky="nsew" ,padx=5, pady=5)

        self.label_income = ttk.Label(self, text="Income : ", anchor="w", font=("Helvetica", 16))
        self.label_income.grid(row=1, column=0, sticky="nsew" ,padx=5, pady=5)

        self.label_income_value = ttk.Label(self, text="0.00", anchor="e", font=("Helvetica", 16), foreground="green")
        self.label_income_value.grid(row=1, column=1, sticky="nsew" ,padx=5, pady=5)

        self.label_expense = ttk.Label(self, text="Expense : ", anchor="w", font=("Helvetica", 16))
        self.label_expense.grid(row=2, column=0, sticky="nsew" ,padx=5, pady=5)

        self.label_expense_value = ttk.Label(self, text="0.00", anchor="e", font=("Helvetica", 16), foreground="red")
        self.label_expense_value.grid(row=2, column=1, sticky="nsew" ,padx=5, pady=5)

        self.label_remain = ttk.Label(self, text="Remain : ", anchor="w", font=("Helvetica", 16))
        self.label_remain.grid(row=3, column=0, sticky="nsew" ,padx=5, pady=5)

        self.label_remain_value = ttk.Label(self, text="0.00", anchor="e", font=("Helvetica", 16))
        self.label_remain_value.grid(row=3, column=1, sticky="nsew" ,padx=5, pady=5)

    
    def setIncome(self, income):
        self.label_income_value.configure(text="{:,.2f}".format(income))

    def setExpense(self, expense):
        self.label_expense_value.configure(text="{:,.2f}".format(expense))
                                    
    def setRemain(self, remain):
        self.label_remain_value.configure(text="{:,.2f}".format(remain))

    def setSummary(self, income, expense, remain):
        self.setIncome(income)
        self.setExpense(expense)
        self.setRemain(remain)